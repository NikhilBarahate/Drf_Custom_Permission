from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsReadonly(BasePermission):
    def has_permission(self, request, view):
        print(view)
        if request.method in SAFE_METHODS:
            return True
        else:
            return False

class IsGetPostPut(BasePermission):
    def has_permission(self, request, view):
        allowed_methods = ['GET', 'POST', 'PUT']
        if request.method in allowed_methods:
            return True
        else:
            return False

class RolePermissions(BasePermission):
    def has_permission(self, request, view):
        status = request.user.is_superuser
        print(status)
        if status == True:
            allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
            if request.method in allowed_methods:
                return True
            else:
                if request.method in SAFE_METHODS:
                    return True