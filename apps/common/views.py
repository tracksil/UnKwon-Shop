from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.common.serializers import CommonHealthSerializer


class CommonViewSet(GenericViewSet):
    serializer_class = CommonHealthSerializer

    @action(detail=False, methods=["GET"], permission_classes=[AllowAny])
    def health(self, request):
        return Response(self.get_serializer().data)

    @action(detail=False, methods=["GET"])
    def protected(self, request):
        return Response(self.get_serializer().data)
