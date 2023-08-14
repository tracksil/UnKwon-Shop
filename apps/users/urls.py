from rest_framework.routers import DefaultRouter

from apps.users.views import UserAuthenticationViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"users", UserAuthenticationViewSet, basename="authentication")

urlpatterns = [*router.urls]
