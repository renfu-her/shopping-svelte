from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List, Optional
from app.core.database import get_db
from app.models.product import Product
from app.models.product_category import ProductCategory
from pydantic import BaseModel
from math import ceil

router = APIRouter()


class ProductResponse(BaseModel):
    id: int
    name: str
    slug: str
    description: str | None
    price: float
    stock: int
    image_url: str | None
    feature_product: bool
    category_id: int

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    items: List[ProductResponse]
    total: int
    page: int
    pages: int
    per_page: int


@router.get("/products", response_model=ProductListResponse)
async def get_products(
    page: int = Query(1, ge=1),
    per_page: int = Query(12, ge=1, le=100),
    category_slug: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    """取得產品列表（支援分頁、分類篩選）"""
    query = db.query(Product)
    
    # 如果有分類篩選
    if category_slug:
        category = db.query(ProductCategory).filter(ProductCategory.slug == category_slug).first()
        if category:
            # 只顯示第三層分類的產品
            if category.level == 3:
                query = query.filter(Product.category_id == category.id)
            else:
                # 如果是第一或二層，取得所有子分類的產品
                def get_all_child_ids(cat_id):
                    children = db.query(ProductCategory).filter(ProductCategory.parent_id == cat_id).all()
                    ids = [cat_id]
                    for child in children:
                        ids.extend(get_all_child_ids(child.id))
                    return ids
                
                category_ids = get_all_child_ids(category.id)
                query = query.filter(Product.category_id.in_(category_ids))
    
    total = query.count()
    pages = ceil(total / per_page) if total > 0 else 0
    
    products = query.order_by(Product.id.desc()).offset((page - 1) * per_page).limit(per_page).all()
    
    return ProductListResponse(
        items=[ProductResponse.model_validate(p) for p in products],
        total=total,
        page=page,
        pages=pages,
        per_page=per_page
    )


@router.get("/products/featured", response_model=List[ProductResponse])
async def get_featured_products(db: Session = Depends(get_db)):
    """取得 9 筆特色產品"""
    products = db.query(Product).filter(Product.feature_product == True).limit(9).all()
    return [ProductResponse.model_validate(p) for p in products]


@router.get("/product/{slug}", response_model=ProductResponse)
async def get_product(slug: str, db: Session = Depends(get_db)):
    """取得產品詳情"""
    product = db.query(Product).filter(Product.slug == slug).first()
    if not product:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductResponse.model_validate(product)

