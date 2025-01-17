from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST

# Create your views here.

# def home(request):
#     return HttpResponse("<h1>Hello World</h1>")


def home(request):
    todo_list=Todo.objects.order_by('id')
    form=TodoForm()
    context={'todo_list':todo_list,'form':form}
    return render(request,'todo/index.html',context)
@require_POST
def addtodo(request):
    form=TodoForm(request.POST)
    print(request.POST['text'])
    if form.is_valid:
        new_todo=Todo(text=request.POST['text'])
        new_todo.save()
    return redirect('Home')
def completetodo(request,todo_id):
    todo=Todo.objects.get(pk=todo_id)
    todo.complete=True
    todo.save()
    return redirect('Home')

def deletecomplete(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('Home')
    
def deleteall(request):
    Todo.objects.all().delete()
    return redirect('Home')