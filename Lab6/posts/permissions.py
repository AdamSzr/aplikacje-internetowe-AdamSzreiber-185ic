from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS: # which is a tuple containing 'GET', 'OPTIONS' and 'HEAD'
            return True

        # Write permissions are only allowed to the author of a post
        return obj.author == request.user
