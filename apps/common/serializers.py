from rest_framework import serializers


class CommonHealthSerializer(serializers.Serializer):
    data = {"live": True}
