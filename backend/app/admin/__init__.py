from fastapi_amis_admin.admin import AdminSite
from fastapi_amis_admin.amis.components import PageSchema
from .models import (
    AdsAdmin,
    UserAdmin,
    ProductCategoryAdmin,
    ProductAdmin,
    CartAdmin,
    CartItemAdmin,
    OrderAdmin,
    OrderItemAdmin,
    NewsAdmin,
    AboutUsAdmin,
    FAQAdmin,
)

def setup_admin(site: AdminSite):
    """設定管理後台"""
    # 註冊所有管理介面
    site.register_admin(AdsAdmin)
    site.register_admin(UserAdmin)
    site.register_admin(ProductCategoryAdmin)
    site.register_admin(ProductAdmin)
    site.register_admin(CartAdmin)
    site.register_admin(CartItemAdmin)
    site.register_admin(OrderAdmin)
    site.register_admin(OrderItemAdmin)
    site.register_admin(NewsAdmin)
    site.register_admin(AboutUsAdmin)
    site.register_admin(FAQAdmin)

