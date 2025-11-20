uv sync# Shopping Cart Backend

## 安裝

使用 uv 安裝依賴：

```bash
cd backend
uv sync
```

這會根據 `pyproject.toml` 自動建立虛擬環境並安裝所有依賴。

## 資料庫設定

1. 確保 MySQL 已安裝並運行

2. 複製環境變數範例檔案：
   ```bash
   cp .env.example .env
   ```

3. 編輯 `.env` 檔案，設定資料庫連線資訊：
   ```env
   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=root
   DB_PASSWORD=
   DB_NAME=shopping-svelte
   ```

4. 初始化資料庫（自動建立資料庫和資料表）：
   ```bash
   uv run python -m app.core.init_db
   ```

   這會自動：
   - 建立資料庫（如果不存在）
   - 建立所有必要的資料表

## 執行

使用 uv 執行（推薦）：

```bash
cd backend
uv run python -m app.main
```

或使用 uvicorn：

```bash
uv run uvicorn app.main:app --reload
```

或直接使用 uvicorn（需先啟動虛擬環境）：

```bash
uvicorn app.main:app --reload
```

API 文件: http://localhost:8000/docs
管理後台: http://localhost:8000/admin

