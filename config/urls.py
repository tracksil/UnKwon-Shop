from django.urls import include, path
from drf_util.utils import get_applications, get_custom_schema_view
from rest_framework_simplejwt.views import TokenRefreshView

schema_view = get_custom_schema_view(title="UnKnown Shop", description="This is API for UnKnown Shop")

urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),  # noqa
    *[
        path("", include(app_urls))
        for app_urls in get_applications(inside_file="urls.py", only_directory=False)
    ],
]

urlpatterns += [path("users/refresh/token/", TokenRefreshView.as_view(), name="token_refresh")]
