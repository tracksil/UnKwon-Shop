from django.db.models import Count
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.common.permissions import IsSuperUser
from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.annotate(
        added_to_wish_list=Count("wishlistproducts__wish_list__user", distinct=True)
    )
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsSuperUser]
        return [permission() for permission in permission_classes]
