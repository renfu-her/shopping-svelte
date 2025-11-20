# Shopping Cart System

完整的購物車系統，包含 FastAPI 後端和 SvelteKit 前端。

## 技術棧

- **後端**: FastAPI, SQLAlchemy, fastapi-amis-admin, MySQL
- **前端**: SvelteKit
- **工具**: uv (Python 套件管理)

## 專案結構

```
shopping-svelte/
├── backend/          # FastAPI 後端
│   ├── app/
│   │   ├── models/   # 資料庫模型
│   │   ├── api/      # API 端點
│   │   ├── admin/    # 管理後台
│   │   └── core/     # 核心設定
│   └── static/       # 靜態檔案（上傳的圖片）
└── frontend/         # SvelteKit 前端
    └── src/
        ├── routes/   # 頁面路由
        └── lib/      # 共用元件和工具
```

## 快速開始

### 後端設定

1. 確保 MySQL 已安裝並運行

2. 安裝依賴：
   ```bash
   cd backend
   uv sync
   ```
   
   這會根據 `pyproject.toml` 自動建立虛擬環境並安裝所有依賴。

3. 設定環境變數：
   ```bash
   cp .env.example .env
   ```
   
   編輯 `.env` 檔案，設定資料庫連線資訊。

4. 初始化資料庫：
   ```bash
   uv run python -m app.core.init_db
   ```
   
   這會自動建立資料庫和所有必要的資料表。

4. 啟動後端：
   ```bash
   uv run uvicorn app.main:app --reload
   ```
   
   或使用 uv 執行：
   ```bash
   uv run python -m app.main
   ```

後端將運行在 http://localhost:8000
- API 文件: http://localhost:8000/docs
- 管理後台: http://localhost:8000/admin

### 前端設定

1. 進入前端目錄：
   ```bash
   cd frontend
   ```

2. 安裝依賴（**請使用 pnpm**，npm 在您的系統上有兼容性問題）：
   ```bash
   pnpm install
   ```
   
   批准構建腳本：
   ```bash
   pnpm approve-builds
   pnpm install
   ```
   
   如果 pnpm 不可用，可以使用 yarn：
   ```bash
   yarn install
   ```

3. 初始化 SvelteKit（首次運行）：
   ```bash
   pnpm run sync
   ```

4. 啟動開發伺服器：
   ```bash
   pnpm dev
   ```

前端將運行在 http://localhost:5000

**注意**：
- 請確保在 `frontend` 目錄下執行這些命令
- 建議使用 `pnpm` 而不是 `npm`（npm 會出現兼容性錯誤）

## 功能

### 後端功能
- RESTful API
- 圖片上傳（自動轉換為 WebP，UUID 命名）
- 管理後台（fastapi-amis-admin）
- 購物車系統（支援訪客和用戶）
- 訂單管理

### 前端功能
- 首頁（Banner 輪播、分類選擇器、特色產品）
- 產品列表（三層分類樹、分頁）
- 產品詳情
- 購物車
- 結帳
- 新聞、關於我們、FAQ

## 資料庫模型

- Ads (Banner)
- Users
- ProductCategory (三層結構)
- Product
- Cart / CartItem
- Order / OrderItem
- News
- AboutUs
- FAQ

## 開發說明

### 圖片上傳
圖片會自動轉換為 WebP 格式，並使用 UUID 命名，儲存在 `backend/static/uploads/` 目錄。

### 產品分類
產品分類採用三層結構（自關聯），只有第三層分類可以包含產品。

### 購物車
支援訪客購物車（基於 session），登入後可合併購物車內容。

