from fastapi_amis_admin.admin import admin
from fastapi_amis_admin.crud import SqlalchemyCrud
from fastapi_amis_admin.amis.components import PageSchema, Form, TableColumn, InputImage, InputNumber, InputText, Textarea, Select, Switch
from app.models import (
    Ads, User, ProductCategory, Product, Cart, CartItem, Order, OrderItem, News, AboutUs, FAQ
)
from app.core.database import engine


class AdsAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="Banner 管理", icon="fa fa-image")
    model = Ads
    engine = engine
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="title", label="標題"),
        TableColumn(name="image_url", label="圖片", type="image"),
        TableColumn(name="link_url", label="連結網址"),
        TableColumn(name="order", label="排序"),
        TableColumn(name="is_active", label="啟用", type="switch"),
        TableColumn(name="created_at", label="建立時間"),
        TableColumn(name="updated_at", label="更新時間"),
    ]
    form = Form(
        body=[
            InputText(name="title", label="標題", required=True),
            InputImage(name="image_url", label="圖片", required=True),
            InputText(name="link_url", label="連結網址"),
            InputNumber(name="order", label="排序", value=0),
            Switch(name="is_active", label="啟用", value=True),
        ]
    )


class UserAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="用戶管理", icon="fa fa-users")
    model = User
    engine = engine
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="username", label="用戶名"),
        TableColumn(name="email", label="電子郵件"),
        TableColumn(name="is_admin", label="管理員", type="switch"),
        TableColumn(name="created_at", label="建立時間"),
        TableColumn(name="updated_at", label="更新時間"),
    ]
    form = Form(
        body=[
            InputText(name="username", label="用戶名", required=True),
            InputText(name="email", label="電子郵件", required=True),
            InputText(name="password_hash", label="密碼雜湊", required=True),
            Switch(name="is_admin", label="管理員", value=False),
        ]
    )


class ProductCategoryAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="產品分類", icon="fa fa-folder")
    model = ProductCategory
    engine = engine
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="name", label="分類名稱"),
        TableColumn(name="slug", label="網址代碼"),
        TableColumn(name="parent_id", label="父分類ID"),
        TableColumn(name="level", label="層級"),
        TableColumn(name="order", label="排序"),
        TableColumn(name="created_at", label="建立時間"),
        TableColumn(name="updated_at", label="更新時間"),
    ]
    form = Form(
        body=[
            InputText(name="name", label="分類名稱", required=True),
            InputText(name="slug", label="網址代碼", required=True),
            InputNumber(name="parent_id", label="父分類ID"),
            InputNumber(name="level", label="層級", value=1),
            InputNumber(name="order", label="排序", value=0),
        ]
    )


class ProductAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="產品管理", icon="fa fa-box")
    model = Product
    engine = engine
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="name", label="產品名稱"),
        TableColumn(name="slug", label="網址代碼"),
        TableColumn(name="price", label="價格"),
        TableColumn(name="stock", label="庫存"),
        TableColumn(name="image_url", label="圖片", type="image"),
        TableColumn(name="feature_product", label="特色產品", type="switch"),
        TableColumn(name="category_id", label="分類ID"),
        TableColumn(name="created_at", label="建立時間"),
        TableColumn(name="updated_at", label="更新時間"),
    ]
    form = Form(
        body=[
            InputText(name="name", label="產品名稱", required=True),
            InputText(name="slug", label="網址代碼", required=True),
            Textarea(name="description", label="描述"),
            InputNumber(name="price", label="價格", required=True),
            InputNumber(name="stock", label="庫存", value=0),
            InputImage(name="image_url", label="圖片"),
            Switch(name="feature_product", label="特色產品", value=False),
            InputNumber(name="category_id", label="分類ID", required=True),
        ]
    )


class CartAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="購物車", icon="fa fa-shopping-cart")
    model = Cart
    engine = engine
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="user_id", label="用戶ID"),
        TableColumn(name="session_id", label="會話ID"),
        TableColumn(name="created_at", label="建立時間"),
        TableColumn(name="updated_at", label="更新時間"),
    ]
    form = Form(
        body=[
            InputNumber(name="user_id", label="用戶ID"),
            InputText(name="session_id", label="會話ID"),
        ]
    )


class CartItemAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="購物車項目", icon="fa fa-list")
    model = CartItem
    engine = engine
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="cart_id", label="購物車ID"),
        TableColumn(name="product_id", label="產品ID"),
        TableColumn(name="quantity", label="數量"),
        TableColumn(name="created_at", label="建立時間"),
        TableColumn(name="updated_at", label="更新時間"),
    ]
    form = Form(
        body=[
            InputNumber(name="cart_id", label="購物車ID", required=True),
            InputNumber(name="product_id", label="產品ID", required=True),
            InputNumber(name="quantity", label="數量", value=1),
        ]
    )


class OrderAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="訂單管理", icon="fa fa-receipt")
    model = Order
    engine = engine
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="user_id", label="用戶ID"),
        TableColumn(name="session_id", label="會話ID"),
        TableColumn(name="total_amount", label="總金額"),
        TableColumn(name="status", label="狀態"),
        TableColumn(name="shipping_address", label="運送地址"),
        TableColumn(name="created_at", label="建立時間"),
        TableColumn(name="updated_at", label="更新時間"),
    ]
    form = Form(
        body=[
            InputNumber(name="user_id", label="用戶ID"),
            InputText(name="session_id", label="會話ID"),
            InputNumber(name="total_amount", label="總金額", required=True),
            Select(
                name="status",
                label="狀態",
                options=[
                    {"label": "待處理", "value": "pending"},
                    {"label": "已付款", "value": "paid"},
                    {"label": "已出貨", "value": "shipped"},
                    {"label": "已完成", "value": "completed"},
                    {"label": "已取消", "value": "cancelled"},
                ],
                value="pending"
            ),
            Textarea(name="shipping_address", label="運送地址"),
        ]
    )


class OrderItemAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="訂單項目", icon="fa fa-list-alt")
    model = OrderItem
    engine = engine
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="order_id", label="訂單ID"),
        TableColumn(name="product_id", label="產品ID"),
        TableColumn(name="quantity", label="數量"),
        TableColumn(name="price", label="價格"),
        TableColumn(name="created_at", label="建立時間"),
        TableColumn(name="updated_at", label="更新時間"),
    ]
    form = Form(
        body=[
            InputNumber(name="order_id", label="訂單ID", required=True),
            InputNumber(name="product_id", label="產品ID", required=True),
            InputNumber(name="quantity", label="數量", required=True),
            InputNumber(name="price", label="價格", required=True),
        ]
    )


class NewsAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="新聞管理", icon="fa fa-newspaper")
    model = News
    engine = engine
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="title", label="標題"),
        TableColumn(name="image_url", label="圖片", type="image"),
        TableColumn(name="published_at", label="發布時間"),
        TableColumn(name="created_at", label="建立時間"),
        TableColumn(name="updated_at", label="更新時間"),
    ]
    form = Form(
        body=[
            InputText(name="title", label="標題", required=True),
            Textarea(name="content", label="內容"),
            InputImage(name="image_url", label="圖片"),
            InputText(name="published_at", label="發布時間", type="datetime-local"),
        ]
    )


class AboutUsAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="關於我們", icon="fa fa-info-circle")
    model = AboutUs
    engine = engine
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="title", label="標題"),
        TableColumn(name="created_at", label="建立時間"),
        TableColumn(name="updated_at", label="更新時間"),
    ]
    form = Form(
        body=[
            InputText(name="title", label="標題", required=True),
            Textarea(name="content", label="內容"),
        ]
    )


class FAQAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="FAQ 管理", icon="fa fa-question-circle")
    model = FAQ
    engine = engine
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="question", label="問題"),
        TableColumn(name="order", label="排序"),
        TableColumn(name="created_at", label="建立時間"),
        TableColumn(name="updated_at", label="更新時間"),
    ]
    form = Form(
        body=[
            InputText(name="question", label="問題", required=True),
            Textarea(name="answer", label="答案", required=True),
            InputNumber(name="order", label="排序", value=0),
        ]
    )
