from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        print(obj.owner.id)
        print(request.user.id)
        return obj.owner.id == request.user.id
          
