from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    added_to_wish_list = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {"sku": {"required": False}}
