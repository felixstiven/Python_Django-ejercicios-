from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200) ## tabla texto
    
    def  __str__(self):
        return self.name

    
class Task(models.Model):
    title = models.CharField(max_length=200)
    descripcion = models.TextField()
    project =  models.ForeignKey(Project, on_delete=models.CASCADE)  
    confirmation = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title + '-' + self.project.name

