import os
import io
import uuid
from pathlib import Path
from fastapi import UploadFile, HTTPException
from PIL import Image
from .config import settings


def ensure_upload_dir():
    """確保上傳目錄存在"""
    upload_path = Path(settings.UPLOAD_DIR)
    upload_path.mkdir(parents=True, exist_ok=True)
    return upload_path


async def save_image_as_webp(file: UploadFile) -> str:
    """
    將上傳的圖片轉換為 webp 格式並儲存
    返回圖片 URL 路徑
    """
    # 檢查檔案類型
    allowed_types = ["image/jpeg", "image/jpg", "image/png", "image/webp"]
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail=f"不支援的檔案類型。支援的類型: {', '.join(allowed_types)}"
        )
    
    # 檢查檔案大小
    contents = await file.read()
    if len(contents) > settings.MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"檔案大小超過限制 ({settings.MAX_UPLOAD_SIZE / 1024 / 1024}MB)"
        )
    
    # 生成 UUID 檔名
    file_extension = "webp"
    filename = f"{uuid.uuid4()}.{file_extension}"
    
    # 確保上傳目錄存在
    upload_dir = ensure_upload_dir()
    file_path = upload_dir / filename
    
    try:
        # 開啟圖片並轉換為 webp
        image = Image.open(io.BytesIO(contents))
        
        # 轉換為 RGB 模式（如果是 RGBA 或其他模式）
        if image.mode in ("RGBA", "LA", "P"):
            # 建立白色背景
            rgb_image = Image.new("RGB", image.size, (255, 255, 255))
            if image.mode == "P":
                image = image.convert("RGBA")
            rgb_image.paste(image, mask=image.split()[-1] if image.mode in ("RGBA", "LA") else None)
            image = rgb_image
        elif image.mode != "RGB":
            image = image.convert("RGB")
        
        # 儲存為 webp
        image.save(file_path, "WEBP", quality=85, optimize=True)
        
        # 返回相對路徑（用於 URL）
        return f"/static/uploads/{filename}"
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"圖片處理失敗: {str(e)}"
        )

