from django.db import models


class KanbanCard(models.Model):
    STATUS_CHOICES = (
        (0, "to-do"),
        (1, "in-progress"),
        (2, "done")
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return f"{self.id} {self.title} {self.description}, {self.get_status_display()}"


class Task(models.Model):
    description = models.CharField(max_length=1000)
    done = models.BooleanField(default=False)

    # connect to KanbanCard
    # each card may have 0 or more tasks
    card = models.ForeignKey(
        KanbanCard,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    def __str__(self):
        return f"id: {self.id}, {self.description}, status: {self.done}, for card {self.kanban_card}"