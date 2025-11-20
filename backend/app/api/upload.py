from fastapi import APIRouter, UploadFile, File, HTTPException
from app.core.upload import save_image_as_webp
from pydantic import BaseModel

router = APIRouter()


class UploadResponse(BaseModel):
    url: str
    message: str


@router.post("/upload", response_model=UploadResponse)
async def upload_image(file: UploadFile = File(...)):
    """上傳圖片並轉換為 webp 格式"""
    try:
        url = await save_image_as_webp(file)
        return UploadResponse(url=url, message="Image uploaded successfully")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

