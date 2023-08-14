from rest_framework import serializers
from .models import WishList, WishListProducts


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = "__all__"
        extra_kwargs = {"user": {"read_only": True}}


class WishListProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishListProducts
        fields = "__all__"
