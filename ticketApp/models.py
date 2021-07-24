from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class tickets(models.Model):
    project = CharField(max_length=20)
    summary = CharField(max_length=200)
    type = CharField(max_length=10, default="")
    assignee = CharField(max_length=30, default="")
    Status = CharField(max_length=10, default="")

    def __str__(self):
        return self.project
