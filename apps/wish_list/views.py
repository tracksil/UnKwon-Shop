from rest_framework import viewsets, generics
from .models import WishList, WishListProducts
from .serializers import WishListSerializer, WishListProductsSerializer


class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return WishList.objects.none()
        return super().get_queryset().filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WishListProductsViewSet(viewsets.ModelViewSet):
    queryset = WishListProducts.objects.all()
    serializer_class = WishListProductsSerializer

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return WishListProducts.objects.none()
        return super().get_queryset().filter(wish_list__user=self.request.user)


class WishListProductsListView(generics.ListAPIView):
    serializer_class = WishListProductsSerializer

    def get_queryset(self):
        wishlist_id = self.kwargs["wishlist_id"]
        return WishListProducts.objects.filter(wish_list=wishlist_id, wish_list__user=self.request.user)
