from django.contrib import admin
from .models import ToDoList
# Register your models here.



class ToDoListAdmin(admin.ModelAdmin):
    list_description = ['description']
    list_due_date = ['due_date']
    list_status = ['status']
    fieldsets =[
        ('Description',{'fields':['list_description']}),
        ('Due Date',{'fields':['list_due_date']}),
        ('Status',{'fields':['status']}),
    ]

admin.site.register(ToDoList)
