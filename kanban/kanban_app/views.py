from rest_framework import generics
from kanban_app.models import KanbanCard, Task
from kanban_app.serializers import KanbanCardSerializer, TaskSerializer

"""
CREATE: POST /tasks
"""
class TaskCollection(generics.CreateAPIView):
    serializer_class = TaskSerializer

"""
Retrieve: GET /tasks/<id>
"""
class TaskRecord(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

"""
Create : POST /cards
LIST: GET /cards
"""
class KanbanCardCollection(generics.ListCreateAPIView):
    queryset = KanbanCard.objects.all()
    serializer_class = KanbanCardSerializer

"""
RETRIEVE: GET /cards/:id
UPDATE: PUT /cards/:id
DESTROY: DELETE /cards/:id
"""
class KanbanCardRecord(generics.RetrieveUpdateDestroyAPIView):
    queryset = KanbanCard.objects.all()
    serializer_class = KanbanCardSerializer
