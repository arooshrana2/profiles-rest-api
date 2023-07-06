from rest_framework import permissions


class UserProfileModify(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
        
        if request.method == permissions.SAFE_METHODS:
            return True
        
        return request.user.id == obj.id
    