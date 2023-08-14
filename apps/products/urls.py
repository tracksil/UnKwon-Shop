from rest_framework.routers import DefaultRouter

from apps.products.views import ProductViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"products", ProductViewSet, basename="products")

urlpatterns = [*router.urls]
