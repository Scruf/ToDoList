from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^new/thankyou/$', views.thankyou, name='thankyou'),
    url(r'^(?P<to_do_list_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<to_do_list_id>[0-9]+)/edit/thankyou/$', views.thankyou_edit, name='thankyou'),
    url(r'^(?P<to_do_list_id>[0-9]+)/delete/$',views.delete, name='delete'),

]
