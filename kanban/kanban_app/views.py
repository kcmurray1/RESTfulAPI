from rest_framework import generics
from kanban_app.models import KanbanCard
from kanban_app.serializers import KanbanCardSerializer

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
