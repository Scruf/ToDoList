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


def new(request):
    new_template = loader.get_template("ToDoList/new.html")
    context={
        'new':'cunt',
    }

    return HttpResponse(new_template.render(context,request))

def thankyou(request):
    if request.method == 'POST':
        description = request.POST.get('description',None)
        due_date = request.POST.get('date',None)
        status = request.POST.get('status',None)
        t = ToDoList(description=description,due_date=due_date,status=status)
        t.save()
        to_do_items = ToDoList.objects.all()
        context = {
            "list":to_do_items,
        }
        thank_you_template = loader.get_template("ToDoList/thankyou.html")
        return HttpResponse(thank_you_template.render(context,request))
