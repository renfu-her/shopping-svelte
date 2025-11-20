# Frontend Setup

## 安裝依賴

由於 npm 可能有兼容性問題，建議使用 pnpm 或 yarn：

### 使用 pnpm（推薦）

```bash
pnpm install
```

### 使用 yarn

```bash
yarn install
```

### 使用 npm（如果可用）

```bash
npm install
```

## 初始化 SvelteKit

首次運行前，需要執行：

```bash
npm run sync
# 或
pnpm sync
# 或
yarn sync
```

這會生成 `.svelte-kit` 目錄和必要的配置文件。

## 開發

```bash
npm run dev
# 或
pnpm dev
# 或
yarn dev
```

前端將運行在 http://localhost:5173

## 注意事項

如果遇到 TypeScript 配置警告，這是正常的。SvelteKit 會在首次運行時自動生成配置文件。

