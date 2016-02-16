from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^ToDoList/', include('ToDoList.urls', namespace="ToDoLists")),
    url(r'^admin/', admin.site.urls),
]
