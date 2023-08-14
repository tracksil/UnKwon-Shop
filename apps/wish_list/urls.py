from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.wish_list.views import WishListViewSet, WishListProductsViewSet, WishListProductsListView

router = DefaultRouter(trailing_slash=False)
router.register(r"wish-list", WishListViewSet, basename="wish_list")
router.register(r"wish-list-products", WishListProductsViewSet, basename="wish_list_products")


urlpatterns = [
    *router.urls,
    path(
        "wishlist-products/<int:wishlist_id>/",
        WishListProductsListView.as_view(),
        name="wishlist-products-list",
    ),
]
