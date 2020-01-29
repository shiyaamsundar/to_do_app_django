from .views import home,addtodo,completetodo,deletecomplete,deleteall
from django.urls import path


urlpatterns = [
    path('',home,name='Home'),
    path('add',addtodo,name='addtodo'),
    path('complete/<todo_id>',completetodo,name='complete'),
    path('delete',deletecomplete,name='delete'),
    path('deleteall',deleteall,name='deleteall'),
    
]
