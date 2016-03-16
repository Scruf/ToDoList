from __future__ import unicode_literals

from django.db import models

class ToDoList(models.Model):
    description = models.CharField(max_length=200)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=10)

    def __str__(self):
        date = self.due_date.day
        month =self. due_date.month
        year = self.due_date.year
        _date=str(date)+"/"+str(month)+"/"+str(year)
        return self.description+"-"+self.status+" "+_date

# Create your models here.
