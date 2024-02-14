from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        print(obj.owner.id)
        print(request.user.id)
        return obj.owner.id == request.user.id

        # Write permissions are only allowed to the owner of the task
          
