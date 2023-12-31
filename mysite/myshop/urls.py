from django.urls import path

from .views import (
    ProfileView,
    ChangePasswordView,
    AvatarView,
    CategoriesView,
    TagView,
    ProductView,
    ReviewView,
    CatalogView,
    ProductsPopularView,
    ProductsLimitedView,
    ProductSaleView,
    ProductBannersSaleView,
    BasketView,
    OrdersView,
    OrderView,
    PaymentView,
)

app_name = "shop"

urlpatterns = [
    path("categories", CategoriesView.as_view()),
    path("catalog", CatalogView.as_view()),
    path("products/popular", ProductsPopularView.as_view()),
    path("products/limited", ProductsLimitedView.as_view()),
    path("sales", ProductSaleView.as_view()),
    path("banners", ProductBannersSaleView.as_view()),

    path("basket", BasketView.as_view()),

    path("orders", OrdersView.as_view()),
    path("order/<int:id>", OrderView.as_view()),

    path("payment/<int:id>", PaymentView.as_view()),

    path("profile", ProfileView.as_view()),
    path("profile/password", ChangePasswordView.as_view()),
    path("profile/avatar", AvatarView.as_view()),

    path("tags", TagView.as_view()),

    path("product/<int:id>", ProductView.as_view()),
    path("product/<int:id>/reviews", ReviewView.as_view()),
]
