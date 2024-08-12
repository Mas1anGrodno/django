from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from mainsite.models import *
from .forms import *

# Create your views here.

def home(request):
    menu = [{'title':'Главная','url':'/'}, 
            {'title':'Проекты','url':'/proj'}, 
            {'title':'Задачи','url':'/tasks'}, 
            {'title':'Войти','url':'/users/login'},
            {'title':'Добавить коментарий','url':'/add_coment'}]
    context = {
        'title': 'Главная страница',
        'menu': menu,
        'footer' : "(c) Максим-Ка - Email: example@example.com",
        'header' : "Главная страница"
        }

    return render(request, 'project_K/home.html',context)

def proj(request):
    menu = [{'title':'Главная','url':'/'}, 
            {'title':'Проекты','url':'/proj'}, 
            {'title':'Задачи','url':'/tasks'}, 
            {'title':'Добавить проект','url':'/add_proj'},
            {'title':'Добавить коментарий','url':'/add_coment'}]
    projects = Project.objects.all()
    
    context = {
        'title': 'Все проекты',
        'menu': menu,
        'projects': projects,
        'footer' : "(c) Максим-Ка - Email: example@example.com",
        'header': "Все Проекты"
        }
    return render(request, 'project_K/proj.html',context)


def coments(request, coment_id):
    menu = [{'title':'Главная','url':'/'}, 
            {'title':'Проекты','url':'/proj'}, 
            {'title':'Задачи','url':'/tasks'}, 
            {'title':'Добавить задачу','url':'/add_task'},
            {'title':'Добавить коментарий','url':'/add_coment'}]
    
    all_coments = Comments.objects.filter(comment_task_id=coment_id)
    context = {
        'title': 'Просмотр Коментариев',
        'menu': menu,
        'all_coments': all_coments,
        'footer' : "(c) Максим-Ка - Email: example@example.com",
        'header' : "Просмотр Коментариев"
    }

    return render(request, 'project_K/coments.html', context)

def add_coment(request):
    menu = [{'title':'Главная','url':'/'}, 
            {'title':'Проекты','url':'/proj'}, 
            {'title':'Задачи','url':'/tasks'}]
           
    
    if request.method == 'POST':
        form = ComentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/')
            except:
                form.add_error(None, 'Ошибка при добавлении проекта')
    else:
        form = ComentsForm()
    
    context = {
        'title': 'Добавление Коментария',
        'menu': menu,
        'form': form,
        'footer' : "(c) Максим-Ка - Email: example@example.com",
        'header' : "Добавление Коментария"
    }
    return render(request, 'project_K/add_coment.html', context)

def tasks(request):
    menu = [{'title':'Главная','url':'/'}, 
            {'title':'Проекты','url':'/proj'}, 
            {'title':'Задачи','url':'/tasks'}, 
            {'title':'Добавить задачу','url':'/add_task'},
            {'title':'Добавить коментарий','url':'/add_coment'}]
    tasks = Tasks.objects.all()

    context = {
        'title': 'Все задачи',
        'menu': menu,
        'tasks': tasks,
        'footer' : "(c) Максим-Ка - Email: example@example.com",
        'header' : "Все Задачи"
        }
    return render(request, 'project_K/tasks.html',context)

def view_task(request, task_id):
    menu = [{'title':'Главная','url':'/'}, 
            {'title':'Проекты','url':'/proj'}, 
            {'title':'Задачи','url':'/tasks'}, 
            {'title':'Добавить задачу','url':'/add_task'},
            {'title':'Добавить коментарий','url':'/add_coment'}]
    
    instance = get_object_or_404(Tasks, id=task_id)
    form = TaskForm(instance=instance)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=instance)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/tasks')
            except:
                form.add_error(None, 'Ошибка при редактировании задачи')

    context = {
        'title': 'Просмотр задачи',
        'menu': menu,
        'form': form,
        'footer' : "(c) Максим-Ка - Email: example@example.com",
        'header' : "Просмотр задачи"
    }
    return render(request, 'project_K/viewtask.html', context)

"""def view_coment(request, task_id):
    instance = get_object_or_404(Comments, id=task_id)
    form = ComentsForm(instance=instance)
    if request.method == 'POST':
        form = ComentsForm(request.POST, instance=instance)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/tasks')
            except:
                form.add_error(None, 'Ошибка при редактировании задачи')
    return render(request, 'project_K/viewtask.html',{'form': form})
"""
def add_proj(request):
    menu = [{'title':'Главная','url':'/'}, 
            {'title':'Проекты','url':'/proj'}, 
            {'title':'Задачи','url':'/tasks'}]
           
    
    if request.method == 'POST':
        form = AddProject(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/proj')
            except:
                form.add_error(None, 'Ошибка при добавлении проекта')
    else:
        form = AddProject()
    
    context = {
        'title': 'Добавление проекта',
        'menu': menu,
        'form': form,
        'footer' : "(c) Максим-Ка - Email: example@example.com",
        'header' : "Добавление проекта"
    }
    return render(request, 'project_K/add_proj.html', context)

def add_task(request):
    menu = [{'title':'Главная','url':'/'}, 
            {'title':'Проекты','url':'/proj'}, 
            {'title':'Задачи','url':'/tasks'}]
            
    
    if request.method == 'POST':
        form = AddTask(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/tasks')
            except:
                form.add_error(None, 'Ошибка при добавлении задачи')
    else:
        form = AddTask()
    
    context = {
        'title': 'Добавление задачи',
        'menu': menu,
        'form': form,
        'footer' : "(c) Максим-Ка - Email: example@example.com",
        'header' : "Добавление задачи"
    }
    return render(request, 'project_K/add_task.html', context)

