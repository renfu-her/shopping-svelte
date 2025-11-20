# Shopping Cart Backend

## 安裝

使用 uv 安裝依賴：

```bash
cd backend
uv sync
```

這會根據 `pyproject.toml` 自動建立虛擬環境並安裝所有依賴。

## 資料庫設定

確保 MySQL 已安裝並運行，資料庫 `shopping-svelte` 已建立。

連線資訊：
- 用戶名: root
- 密碼: (空)
- 資料庫: shopping-svelte

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

