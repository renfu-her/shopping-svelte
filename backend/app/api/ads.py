from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.ads import Ads
from pydantic import BaseModel

router = APIRouter()


class AdsResponse(BaseModel):
    id: int
    title: str
    image_url: str
    link_url: str | None

    class Config:
        from_attributes = True


@router.get("/ads", response_model=List[AdsResponse])
async def get_ads(db: Session = Depends(get_db)):
    """取得首頁 Banner"""
    ads = db.query(Ads).filter(Ads.is_active == True).order_by(Ads.order).all()
    return [AdsResponse.model_validate(ad) for ad in ads]

