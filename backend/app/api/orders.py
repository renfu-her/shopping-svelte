from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional, List
from app.core.database import get_db
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.product import Product
from pydantic import BaseModel
from fastapi import Header
from decimal import Decimal

router = APIRouter()


class CreateOrderRequest(BaseModel):
    shipping_address: str


class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    price: float
    product: dict

    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    id: int
    total_amount: float
    status: str
    shipping_address: str | None
    items: List[OrderItemResponse]

    class Config:
        from_attributes = True


@router.post("/orders", response_model=OrderResponse)
async def create_order(
    request: CreateOrderRequest,
    x_session_id: Optional[str] = Header(None, alias="X-Session-Id"),
    user_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """建立訂單"""
    # 取得購物車
    if user_id:
        cart = db.query(Cart).filter(Cart.user_id == user_id).first()
    elif x_session_id:
        cart = db.query(Cart).filter(Cart.session_id == x_session_id).first()
    else:
        raise HTTPException(status_code=400, detail="No cart found")
    
    if not cart or not cart.items:
        raise HTTPException(status_code=400, detail="Cart is empty")
    
    # 計算總金額
    total_amount = Decimal("0.00")
    for item in cart.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if product:
            total_amount += Decimal(str(product.price)) * item.quantity
    
    # 建立訂單
    order = Order(
        user_id=user_id,
        session_id=x_session_id,
        total_amount=total_amount,
        status="pending",
        shipping_address=request.shipping_address
    )
    db.add(order)
    db.flush()
    
    # 建立訂單項目
    for item in cart.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if product:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=product.price
            )
            db.add(order_item)
    
    # 清空購物車
    db.query(CartItem).filter(CartItem.cart_id == cart.id).delete()
    db.delete(cart)
    
    db.commit()
    db.refresh(order)
    
    # 取得訂單項目
    order_items = db.query(OrderItem).filter(OrderItem.order_id == order.id).all()
    items = []
    for item in order_items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        items.append(OrderItemResponse(
            id=item.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=float(item.price),
            product={
                "id": product.id,
                "name": product.name,
                "slug": product.slug,
                "image_url": product.image_url
            } if product else {}
        ))
    
    return OrderResponse(
        id=order.id,
        total_amount=float(order.total_amount),
        status=order.status,
        shipping_address=order.shipping_address,
        items=items
    )

