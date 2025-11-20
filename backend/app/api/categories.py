from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.product_category import ProductCategory
from pydantic import BaseModel

router = APIRouter()


class CategoryResponse(BaseModel):
    id: int
    name: str
    slug: str
    parent_id: int | None
    level: int
    order: int
    children: List["CategoryResponse"] = []

    class Config:
        from_attributes = True


CategoryResponse.model_rebuild()


@router.get("/categories", response_model=List[CategoryResponse])
async def get_categories(db: Session = Depends(get_db)):
    """取得分類樹狀結構"""
    categories = db.query(ProductCategory).order_by(ProductCategory.level, ProductCategory.order).all()
    
    # 建立 id 到 category 的映射
    category_map = {}
    for cat in categories:
        category_map[cat.id] = CategoryResponse(
            id=cat.id,
            name=cat.name,
            slug=cat.slug,
            parent_id=cat.parent_id,
            level=cat.level,
            order=cat.order,
            children=[]
        )
    
    # 建立樹狀結構
    root_categories = []
    for cat in categories:
        category_response = category_map[cat.id]
        if cat.parent_id is None:
            root_categories.append(category_response)
        else:
            if cat.parent_id in category_map:
                category_map[cat.parent_id].children.append(category_response)
    
    return root_categories

