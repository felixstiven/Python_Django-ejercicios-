# from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask


# Create your views here.
def index (request):
    title = 'Welcome Django Course'
    return render(request,'index.html', {
        'title': title
    })

def about (request):
    return render(request,'about.html')

def hello(request, username): 
    print(username)
    return HttpResponse('<h1>hello %s</h1<' % username)

def projects (request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects' : projects
    })

def tasks(request):
    #task = Task.objects.get(title = title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })
    
def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        }) 
    else: 
        Task.objects.create(title=request.POST['title'], descripcion=request.POST['descripcion'], project_id=1)
        return redirect('/tasks/') 
def create_project(request):
    return render(request, 'projects/create_project.html')


