"""
資料庫初始化腳本
用於自動建立資料庫和資料表
"""
import sys
from sqlalchemy import create_engine, text
from app.core.config import settings
from app.core.database import Base, engine
from app.models import *  # 導入所有模型以確保 Base.metadata 包含所有表


def create_database():
    """建立資料庫（如果不存在）"""
    # 連接到 MySQL 伺服器（不指定資料庫）
    admin_engine = create_engine(
        settings.DATABASE_URL_WITHOUT_DB,
        pool_pre_ping=True,
        echo=False
    )
    
    try:
        with admin_engine.connect() as conn:
            # 檢查資料庫是否存在（使用參數化查詢）
            result = conn.execute(
                text("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = :db_name"),
                {"db_name": settings.DB_NAME}
            )
            exists = result.fetchone()
            
            if not exists:
                # 建立資料庫（資料庫名稱需要直接拼接，但已從配置檔案驗證）
                # 使用反引號避免特殊字元問題
                db_name_escaped = settings.DB_NAME.replace('`', '``')
                conn.execute(text(f"CREATE DATABASE `{db_name_escaped}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"))
                conn.commit()
                print(f"✓ 資料庫 '{settings.DB_NAME}' 已建立")
            else:
                print(f"✓ 資料庫 '{settings.DB_NAME}' 已存在")
    except Exception as e:
        print(f"✗ 建立資料庫時發生錯誤: {e}")
        sys.exit(1)
    finally:
        admin_engine.dispose()


def create_tables():
    """建立所有資料表"""
    try:
        Base.metadata.create_all(bind=engine)
        print("✓ 所有資料表已建立")
    except Exception as e:
        print(f"✗ 建立資料表時發生錯誤: {e}")
        sys.exit(1)


def main():
    """主函數"""
    print("開始初始化資料庫...")
    print(f"資料庫主機: {settings.DB_HOST}:{settings.DB_PORT}")
    print(f"資料庫名稱: {settings.DB_NAME}")
    print()
    
    # 建立資料庫
    create_database()
    
    # 建立資料表
    create_tables()
    
    print()
    print("✓ 資料庫初始化完成！")


if __name__ == "__main__":
    main()

