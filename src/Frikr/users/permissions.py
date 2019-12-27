from rest_framework.permissions import BasePermission
import users.api

class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Defines if authenticated user in request.user has permissions to act (GET, POST PUT or DELETE)
        """
        if request.method == "POST": #creating user. Anyone can register
            return True
        elif request.user.is_superuser: #superusers are allowed free access
            return True
        elif isinstance(view, users.api.UserDetailAPI): 
            # action is GET PUT or DELETE and user is not superuser.
            # PUT and DELETE are relegated to object permissions
            # if GET is access to detail, relegate to object permissions, if GET is access to listing then not allow
            return True 
        else: 
            return False

    def has_object_permission(self, request, view, obj):
        """
        Defines if authenticated user in request.user has permissions to act (GET, POST PUT or DELETE) on object obj
        """
        # if it's superuser it can access everything
        # if not, then authenticated user can only act on itself
        return request.user.is_superuser or request.user == obj