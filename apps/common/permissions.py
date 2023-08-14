from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    message = _("You do not have permission to perform this action.")

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsSuperUser(BasePermission):
    message = _("You do not have permission to perform this action.")

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
