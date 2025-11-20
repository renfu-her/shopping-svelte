from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.news import News
from pydantic import BaseModel

router = APIRouter()


from datetime import datetime

class NewsResponse(BaseModel):
    id: int
    title: str
    content: str | None
    image_url: str | None
    published_at: datetime | None
    created_at: datetime

    class Config:
        from_attributes = True


@router.get("/news", response_model=List[NewsResponse])
async def get_news(db: Session = Depends(get_db)):
    """取得新聞列表"""
    news_list = db.query(News).order_by(News.published_at.desc(), News.created_at.desc()).all()
    return [NewsResponse.model_validate(n) for n in news_list]

