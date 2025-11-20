from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional, List
from app.core.database import get_db
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.product import Product
from pydantic import BaseModel
from fastapi import Header

router = APIRouter()


class CartItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    product: dict

    class Config:
        from_attributes = True


class CartResponse(BaseModel):
    id: int
    items: List[CartItemResponse]
    total_amount: float

    class Config:
        from_attributes = True


class AddCartItemRequest(BaseModel):
    product_id: int
    quantity: int = 1


class UpdateCartItemRequest(BaseModel):
    quantity: int


def get_or_create_cart(db: Session, user_id: Optional[int] = None, session_id: Optional[str] = None) -> Cart:
    """取得或建立購物車"""
    if user_id:
        cart = db.query(Cart).filter(Cart.user_id == user_id).first()
    elif session_id:
        cart = db.query(Cart).filter(Cart.session_id == session_id).first()
    else:
        cart = None
    
    if not cart:
        cart = Cart(user_id=user_id, session_id=session_id)
        db.add(cart)
        db.commit()
        db.refresh(cart)
    
    return cart


@router.get("/cart", response_model=CartResponse)
async def get_cart(
    x_session_id: Optional[str] = Header(None, alias="X-Session-Id"),
    user_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """取得購物車"""
    cart = get_or_create_cart(db, user_id=user_id, session_id=x_session_id)
    
    items = []
    total_amount = 0.0
    
    for item in cart.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if product:
            items.append(CartItemResponse(
                id=item.id,
                product_id=item.product_id,
                quantity=item.quantity,
                product={
                    "id": product.id,
                    "name": product.name,
                    "slug": product.slug,
                    "price": float(product.price),
                    "image_url": product.image_url
                }
            ))
            total_amount += float(product.price) * item.quantity
    
    return CartResponse(
        id=cart.id,
        items=items,
        total_amount=total_amount
    )


@router.post("/cart/items")
async def add_cart_item(
    request: AddCartItemRequest,
    x_session_id: Optional[str] = Header(None, alias="X-Session-Id"),
    user_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """新增購物車項目"""
    cart = get_or_create_cart(db, user_id=user_id, session_id=x_session_id)
    
    # 檢查產品是否存在
    product = db.query(Product).filter(Product.id == request.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # 檢查是否已有該產品
    existing_item = db.query(CartItem).filter(
        CartItem.cart_id == cart.id,
        CartItem.product_id == request.product_id
    ).first()
    
    if existing_item:
        existing_item.quantity += request.quantity
    else:
        new_item = CartItem(
            cart_id=cart.id,
            product_id=request.product_id,
            quantity=request.quantity
        )
        db.add(new_item)
    
    db.commit()
    return {"message": "Item added to cart"}


@router.put("/cart/items/{item_id}")
async def update_cart_item(
    item_id: int,
    request: UpdateCartItemRequest,
    x_session_id: Optional[str] = Header(None, alias="X-Session-Id"),
    user_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """更新購物車項目"""
    cart = get_or_create_cart(db, user_id=user_id, session_id=x_session_id)
    
    item = db.query(CartItem).filter(
        CartItem.id == item_id,
        CartItem.cart_id == cart.id
    ).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    
    item.quantity = request.quantity
    db.commit()
    return {"message": "Cart item updated"}


@router.delete("/cart/items/{item_id}")
async def delete_cart_item(
    item_id: int,
    x_session_id: Optional[str] = Header(None, alias="X-Session-Id"),
    user_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """刪除購物車項目"""
    cart = get_or_create_cart(db, user_id=user_id, session_id=x_session_id)
    
    item = db.query(CartItem).filter(
        CartItem.id == item_id,
        CartItem.cart_id == cart.id
    ).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    
    db.delete(item)
    db.commit()
    return {"message": "Cart item deleted"}

