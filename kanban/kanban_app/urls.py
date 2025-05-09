from django.urls import path
from kanban_app.views import KanbanCardRecord, KanbanCardCollection, TaskRecord, TaskCollection

urlpatterns = [
    path("cards", KanbanCardCollection.as_view()),
    path("cards/<int:pk>", KanbanCardRecord.as_view()),
    path("tasks/<int:pk>", TaskRecord.as_view()),
    path("tasks", TaskCollection.as_view())
]