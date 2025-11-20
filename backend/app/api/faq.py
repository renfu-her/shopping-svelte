from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.faq import FAQ
from pydantic import BaseModel

router = APIRouter()


class FAQResponse(BaseModel):
    id: int
    question: str
    answer: str
    order: int

    class Config:
        from_attributes = True


@router.get("/faq", response_model=List[FAQResponse])
async def get_faq(db: Session = Depends(get_db)):
    """取得 FAQ 列表"""
    faqs = db.query(FAQ).order_by(FAQ.order).all()
    return [FAQResponse.model_validate(faq) for faq in faqs]

