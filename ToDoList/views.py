from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ToDoList
# Create your views here.
def index(request):
    to_do_items = ToDoList.objects.all()
    templte = loader.get_template("ToDoList/index.html")
    context = {
        'list_t':to_do_items,
    }

    return HttpResponse(templte.render(context,request))
