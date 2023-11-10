from rest_framework import permissions


class IsStaff(permissions.BasePermission):

    edit_methods = ("GET", "PUT", "PATCH")

    def has_permission(self, request, view):
        if permissions.IsAuthenticated and \
                request.user.is_staff:
            return True


    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        # Verifica se l'oggetto ha un attributo "author" prima di accedervi
        if hasattr(obj, 'author') and obj.author == request.user:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False

