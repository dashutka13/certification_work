from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user or request.user.is_staff:
            return True
        return False
