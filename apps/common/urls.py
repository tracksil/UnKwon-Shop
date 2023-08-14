from rest_framework.routers import DefaultRouter
from apps.common.views import CommonViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"common", CommonViewSet, basename="common")

urlpatterns = [*router.urls]
