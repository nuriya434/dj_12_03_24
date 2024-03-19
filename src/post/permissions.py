# post/permissions.py

from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Пользователь может редактировать или удалять только свои собственные объекты.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешить GET, HEAD или OPTIONS запросы для любых пользователей.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Разрешить редактирование или удаление только владельцу объекта.
        return obj.owner == request.user
