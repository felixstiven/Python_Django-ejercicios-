from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de Tarea", max_length=200)
    descripcion = forms.CharField(label="descripcion de la tarea", widget=forms.Textarea)
    
class CreateNewProject(forms.Form):
    