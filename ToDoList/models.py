from __future__ import unicode_literals

from django.db import models

class ToDoList(models.Model):
    description = models.CharField(max_length=200)
    due_date = models.DateTimeField('date published')
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.description+"-"+self.status+" "

# Create your models here.
