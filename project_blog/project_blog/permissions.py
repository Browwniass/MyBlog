from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission that allow only admin to edit, delete
    and create objects.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `is_staff`.
        return bool(request.user and request.user.is_staff)