from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthenticatedOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or obj.user == request.user and request.user.is_authenticated:
            return True
        return False
