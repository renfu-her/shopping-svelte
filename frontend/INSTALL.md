# 前端安裝說明

## 問題

如果遇到 `npm error Class extends value undefined is not a constructor or null` 錯誤，這是 npm 與 Node.js 版本兼容性問題。

## 解決方案

### 方案 1：使用 pnpm（推薦）

pnpm 已經安裝在您的系統中，請在 **Windows PowerShell 或 CMD** 中執行：

```powershell
cd frontend
pnpm install
```

### 方案 2：使用 yarn

如果 pnpm 不可用，可以安裝 yarn：

```powershell
npm install -g yarn
cd frontend
yarn install
```

### 方案 3：修復 npm

在 **Windows PowerShell 或 CMD** 中執行：

```powershell
# 清除 npm 快取
npm cache clean --force

# 重新安裝 npm
npm install -g npm@latest
```

如果仍然失敗，可能需要重新安裝 Node.js。

## 安裝完成後

執行開發伺服器：

```bash
pnpm dev
```

或使用 yarn：

```bash
yarn dev
```

前端將運行在 http://localhost:5000

**注意**：請使用 `pnpm` 或 `yarn`，不要使用 `npm`。

