from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'you must be owner of this object'
    safe_methods = ['GET', 'PUT']

    def has_permission(self, request, view):
        if request.method in self.safe_methods:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
