from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    """Проверка доступа к удалению и редактированию."""
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
