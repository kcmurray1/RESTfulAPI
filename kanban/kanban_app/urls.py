from django.urls import path
from kanban_app.views import KanbanCardRecord, KanbanCardCollection

urlpatterns = [
    path("cards", KanbanCardCollection.as_view()),
    path("cards/<int:pk>", KanbanCardRecord.as_view())
]