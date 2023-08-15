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

    def validate(self, data):
        user = self.context["request"].user
        wish_list = data["wish_list"]

        if wish_list.user != user:
            raise serializers.ValidationError("You can only add items to your own wish list.")

        return data
