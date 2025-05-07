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
