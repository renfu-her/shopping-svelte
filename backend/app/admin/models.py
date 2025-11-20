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


class UserAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="用戶管理", icon="fa fa-users")
    model = User
    engine = engine


class ProductCategoryAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="產品分類", icon="fa fa-folder")
    model = ProductCategory
    engine = engine


class ProductAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="產品管理", icon="fa fa-box")
    model = Product
    engine = engine


class CartAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="購物車", icon="fa fa-shopping-cart")
    model = Cart
    engine = engine


class CartItemAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="購物車項目", icon="fa fa-list")
    model = CartItem
    engine = engine


class OrderAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="訂單管理", icon="fa fa-receipt")
    model = Order
    engine = engine


class OrderItemAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="訂單項目", icon="fa fa-list-alt")
    model = OrderItem
    engine = engine


class NewsAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="新聞管理", icon="fa fa-newspaper")
    model = News
    engine = engine


class AboutUsAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="關於我們", icon="fa fa-info-circle")
    model = AboutUs
    engine = engine


class FAQAdmin(admin.ModelAdmin):
    page_schema = PageSchema(label="FAQ 管理", icon="fa fa-question-circle")
    model = FAQ
    engine = engine
