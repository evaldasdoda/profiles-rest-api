from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow user to edit their own profile """
    def has_object_permission(self, request, view, obj):
        """ Check user is trying to edit their own profile """
        # HTTP GET is safe method
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if user id matches when trying to edit HTTP PUT/PATCH/DELETE, not SAFE_METHODS
        return obj.id == request.user.id
