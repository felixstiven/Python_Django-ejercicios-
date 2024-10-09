# from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render


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
    return render(request, 'projects.html', {
        'projects' : projects
    })

def tasks(request):
    #task = Task.objects.get(title = title)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })




