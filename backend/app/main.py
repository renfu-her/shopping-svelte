from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.core.config import settings
from app.core.database import engine, Base, SessionLocal
from app.api import categories, products, cart, orders, upload, ads, news, about, faq
from fastapi_amis_admin.admin import AdminSite
from fastapi_amis_admin.admin.settings import Settings as AdminSettings
from app.admin import setup_admin

# 建立資料表（如果資料庫已存在）
try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"警告: 無法建立資料表，請先執行 'uv run python -m app.core.init_db' 初始化資料庫: {e}")

app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
)

# CORS 設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 靜態檔案服務
upload_dir = Path(settings.UPLOAD_DIR)
upload_dir.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 管理後台
try:
    admin_settings = AdminSettings()
    site = AdminSite(settings=admin_settings, engine=engine)
    setup_admin(site)
    site.mount_app(app)
except Exception as e:
    print(f"Admin panel setup error: {e}")
    import traceback
    traceback.print_exc()
    # 繼續執行，即使 admin 設定失敗

# API 路由
app.include_router(categories.router, prefix="/api", tags=["categories"])
app.include_router(products.router, prefix="/api", tags=["products"])
app.include_router(cart.router, prefix="/api", tags=["cart"])
app.include_router(orders.router, prefix="/api", tags=["orders"])
app.include_router(upload.router, prefix="/api", tags=["upload"])
app.include_router(ads.router, prefix="/api", tags=["ads"])
app.include_router(news.router, prefix="/api", tags=["news"])
app.include_router(about.router, prefix="/api", tags=["about"])
app.include_router(faq.router, prefix="/api", tags=["faq"])


@app.get("/")
async def root():
    return {"message": "Shopping Cart API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

