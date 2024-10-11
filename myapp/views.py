# from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject


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
        return redirect('tasks') 
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form' : CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    
def project_detail(request, id):
        # Project.objects.get(id = id)
        project = get_object_or_404(Project, id=id)
        tasks = Task.objects.filter(project_id=id)
        return render(request,  'projects/project_detail.html',{
            'project': project,
            'tasks' : tasks
        })



