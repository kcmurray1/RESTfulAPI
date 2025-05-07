from rest_framework import serializers
from kanban_app.models import KanbanCard

class KanbanCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanCard
        fields = '__all__'

