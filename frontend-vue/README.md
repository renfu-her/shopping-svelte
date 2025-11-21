# Vue 3 前端項目

這是使用 Vue 3 構建的購物車系統前端。

## 技術棧

- **Vue 3** - 前端框架
- **Vue Router** - 路由管理
- **Pinia** - 狀態管理
- **Vite** - 構建工具

## 安裝

```bash
cd frontend-vue
pnpm install
# 或
npm install
```

## 開發

```bash
pnpm dev
# 或
npm run dev
```

開發服務器將在 `http://localhost:5000` 啟動。

## 構建

```bash
pnpm build
# 或
npm run build
```

## 項目結構

```
frontend-vue/
├── src/
│   ├── components/      # 可重用組件
│   │   ├── Header.vue
│   │   ├── Footer.vue
│   │   ├── ProductCard.vue
│   │   ├── BannerCarousel.vue
│   │   ├── CategoryTree.vue
│   │   └── CategoryNode.vue
│   ├── views/          # 頁面組件
│   │   ├── HomeView.vue
│   │   ├── ProductListView.vue
│   │   ├── ProductDetailView.vue
│   │   ├── CartView.vue
│   │   ├── CheckoutView.vue
│   │   └── ...
│   ├── layouts/        # 布局組件
│   │   └── DefaultLayout.vue
│   ├── stores/         # Pinia stores
│   │   └── cart.js
│   ├── services/       # API 服務
│   │   └── api.js
│   ├── router/         # 路由配置
│   │   └── index.js
│   ├── App.vue
│   ├── main.js
│   └── style.css
├── index.html
├── vite.config.js
└── package.json
```

## 功能

- ✅ 首頁（Banner 輪播、促銷橫幅、分類、產品標籤頁）
- ✅ 商品列表頁（左側邊欄、網格/列表視圖、分頁）
- ✅ 商品詳情頁（標籤頁、相關產品）
- ✅ 購物車
- ✅ 結帳
- ✅ 關於我們、新聞、FAQ 等頁面

## 與後端 API 集成

前端通過 `/api` 路徑與後端通信。確保後端服務運行在 `http://127.0.0.1:8000`。

Vite 配置中已設置代理：
- `/api` → `http://127.0.0.1:8000/api`
- `/static` → `http://127.0.0.1:8000/static`

