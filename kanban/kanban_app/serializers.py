from rest_framework import serializers
from kanban_app.models import KanbanCard, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class KanbanCardSerializer(serializers.ModelSerializer):

    tasks = TaskSerializer(
        many=True,
        read_only=True,
    )
    
    class Meta:
        model = KanbanCard
        fields = '__all__'

