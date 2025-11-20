from fastapi_amis_admin.admin import admin
from fastapi_amis_admin.crud import SQLAlchemyCrud
from fastapi_amis_admin.amis.components import PageSchema, Form, TableColumn, InputImage, InputNumber, InputText, InputTextArea, Select, Switch
from sqlalchemy import select
from app.models import (
    Ads, User, ProductCategory, Product, Cart, CartItem, Order, OrderItem, News, AboutUs, FAQ
)
from app.core.database import SessionLocal


class AdsAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="Banner 管理", icon="fa fa-image")
    model = Ads
    crud = SQLAlchemyCrud(Ads, SessionLocal)
    
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="title", label="標題"),
        TableColumn(name="image_url", label="圖片", type="image"),
        TableColumn(name="link_url", label="連結"),
        TableColumn(name="order", label="排序"),
        TableColumn(name="is_active", label="啟用", type="switch"),
    ]
    
    form = Form(
        title="Banner 表單",
        body=[
            InputText(name="title", label="標題", required=True),
            InputImage(name="image_url", label="圖片", required=True),
            InputText(name="link_url", label="連結"),
            InputNumber(name="order", label="排序", value=0),
            Switch(name="is_active", label="啟用", value=True),
        ]
    )


class UserAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="用戶管理", icon="fa fa-users")
    model = User
    crud = SQLAlchemyCrud(User, SessionLocal)
    
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="username", label="用戶名"),
        TableColumn(name="email", label="郵箱"),
        TableColumn(name="is_admin", label="管理員", type="switch"),
    ]


class ProductCategoryAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="產品分類", icon="fa fa-folder")
    model = ProductCategory
    crud = SQLAlchemyCrud(ProductCategory, SessionLocal)
    
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="name", label="名稱"),
        TableColumn(name="slug", label="Slug"),
        TableColumn(name="parent_id", label="父分類ID"),
        TableColumn(name="level", label="層級"),
        TableColumn(name="order", label="排序"),
    ]
    
    form = Form(
        title="產品分類表單",
        body=[
            InputText(name="name", label="名稱", required=True),
            InputText(name="slug", label="Slug", required=True),
            InputNumber(name="parent_id", label="父分類ID"),
            InputNumber(name="level", label="層級", value=1),
            InputNumber(name="order", label="排序", value=0),
        ]
    )


class ProductAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="產品管理", icon="fa fa-box")
    model = Product
    crud = SQLAlchemyCrud(Product, SessionLocal)
    
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="name", label="名稱"),
        TableColumn(name="slug", label="Slug"),
        TableColumn(name="price", label="價格"),
        TableColumn(name="stock", label="庫存"),
        TableColumn(name="image_url", label="圖片", type="image"),
        TableColumn(name="feature_product", label="特色產品", type="switch"),
        TableColumn(name="category_id", label="分類ID"),
    ]
    
    form = Form(
        title="產品表單",
        body=[
            InputText(name="name", label="名稱", required=True),
            InputText(name="slug", label="Slug", required=True),
            InputTextArea(name="description", label="描述"),
            InputNumber(name="price", label="價格", required=True),
            InputNumber(name="stock", label="庫存", value=0),
            InputImage(name="image_url", label="圖片"),
            Switch(name="feature_product", label="特色產品"),
            InputNumber(name="category_id", label="分類ID", required=True),
        ]
    )


class CartAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="購物車", icon="fa fa-shopping-cart")
    model = Cart
    crud = SQLAlchemyCrud(Cart, SessionLocal)
    
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="user_id", label="用戶ID"),
        TableColumn(name="session_id", label="Session ID"),
    ]


class CartItemAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="購物車項目", icon="fa fa-list")
    model = CartItem
    crud = SQLAlchemyCrud(CartItem, SessionLocal)
    
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="cart_id", label="購物車ID"),
        TableColumn(name="product_id", label="產品ID"),
        TableColumn(name="quantity", label="數量"),
    ]


class OrderAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="訂單管理", icon="fa fa-receipt")
    model = Order
    crud = SQLAlchemyCrud(Order, SessionLocal)
    
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="user_id", label="用戶ID"),
        TableColumn(name="total_amount", label="總金額"),
        TableColumn(name="status", label="狀態"),
        TableColumn(name="created_at", label="建立時間"),
    ]


class OrderItemAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="訂單項目", icon="fa fa-list-alt")
    model = OrderItem
    crud = SQLAlchemyCrud(OrderItem, SessionLocal)
    
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="order_id", label="訂單ID"),
        TableColumn(name="product_id", label="產品ID"),
        TableColumn(name="quantity", label="數量"),
        TableColumn(name="price", label="價格"),
    ]


class NewsAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="新聞管理", icon="fa fa-newspaper")
    model = News
    crud = SQLAlchemyCrud(News, SessionLocal)
    
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="title", label="標題"),
        TableColumn(name="image_url", label="圖片", type="image"),
        TableColumn(name="published_at", label="發布時間"),
    ]
    
    form = Form(
        title="新聞表單",
        body=[
            InputText(name="title", label="標題", required=True),
            InputTextArea(name="content", label="內容"),
            InputImage(name="image_url", label="圖片"),
        ]
    )


class AboutUsAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="關於我們", icon="fa fa-info-circle")
    model = AboutUs
    crud = SQLAlchemyCrud(AboutUs, SessionLocal)
    
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="title", label="標題"),
    ]
    
    form = Form(
        title="關於我們表單",
        body=[
            InputText(name="title", label="標題", required=True),
            InputTextArea(name="content", label="內容"),
        ]
    )


class FAQAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="FAQ 管理", icon="fa fa-question-circle")
    model = FAQ
    crud = SQLAlchemyCrud(FAQ, SessionLocal)
    
    list_display = [
        TableColumn(name="id", label="ID"),
        TableColumn(name="question", label="問題"),
        TableColumn(name="answer", label="答案"),
        TableColumn(name="order", label="排序"),
    ]
    
    form = Form(
        title="FAQ 表單",
        body=[
            InputText(name="question", label="問題", required=True),
            InputTextArea(name="answer", label="答案", required=True),
            InputNumber(name="order", label="排序", value=0),
        ]
    )

