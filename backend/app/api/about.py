from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.about_us import AboutUs
from pydantic import BaseModel

router = APIRouter()


class AboutResponse(BaseModel):
    id: int
    title: str
    content: str | None

    class Config:
        from_attributes = True


@router.get("/about", response_model=AboutResponse)
async def get_about(db: Session = Depends(get_db)):
    """取得關於我們"""
    about = db.query(AboutUs).first()
    if not about:
        raise HTTPException(status_code=404, detail="About us not found")
    return AboutResponse.model_validate(about)

