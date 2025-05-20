from rest_framework import generics, permissions
from kanban_app.models import KanbanCard, Task
from kanban_app.serializers import KanbanCardSerializer, TaskSerializer

# Auth packages
from kanban_app.customer_permissions import IsKanbanCardOwnerPermission, IsOwnerPermission
from django.core import exceptions

"""
CREATE: POST /tasks
"""
class TaskCollection(generics.CreateAPIView):
    serializer_class = TaskSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]
    
    # Only authenticated Owner can update their tasks
    def perform_create(self, serializer: TaskSerializer):
        card_owner = serializer.validated_data['card'].owner
        auth_user = self.request.user
        if card_owner == auth_user:
            serializer.save()
        else:
            raise exceptions.PermissionDenied

"""
Retrieve: GET /tasks/<id>
"""
class TaskRecord(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    permission_classes = [
        permissions.IsAuthenticated,
        IsKanbanCardOwnerPermission
    ]

"""
Create : POST /cards
LIST: GET /cards
"""
class KanbanCardCollection(generics.ListCreateAPIView):
    serializer_class = KanbanCardSerializer

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    # Only retrieve cards of authenticated Owner
    def get_queryset(self):
        auth_user = self.request.user
        return KanbanCard.objects.filter(owner=auth_user)
    
    # Add cards to Authenticated Owner
    def perform_create(self, serializer : KanbanCardSerializer):
        auth_user = self.request.user
        serializer.save(owner=auth_user)

"""
RETRIEVE: GET /cards/:id
UPDATE: PUT /cards/:id
DESTROY: DELETE /cards/:id
"""
class KanbanCardRecord(generics.RetrieveUpdateDestroyAPIView):
    queryset = KanbanCard.objects.all()
    serializer_class = KanbanCardSerializer

    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerPermission
    ]
