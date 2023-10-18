from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Project(models.Model):
    nombre= models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    fechaInicio = models.DateTimeField(auto_now_add=True)
    fechaTermino = models.DateTimeField(null=True, blank=True)
    proyecto_cerrado = models.BooleanField(default=False)
    admin= models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    members = models.ManyToManyField(User, through="ProjectMembers")
    
    def __str__(self):
        return self.nombre + " || \t || " + "Admin: " + self.admin.username

class Stage(models.Model):
    nombre= models.CharField(max_length=50)
    project= models.ForeignKey(Project, on_delete=models.CASCADE)
    color= models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre + " ||\t Project: \t|| " + self.project.nombre

class ProjectMembers(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='Project')
    date_joined = models.DateTimeField(auto_now_add=True)
    charge = models.CharField(max_length=64, null=True)
    
    def __str__(self):
        return self.person.username + " || \t || " + self.project.nombre

class ProjectTask(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fechaInicio = models.DateTimeField()
    fechaTermino = models.DateTimeField(null=True, blank=True)
    etiquetas= models.CharField(max_length=100, null=True, blank=True)
    importancia= models.CharField(max_length=100, null=True, blank=True)
    encargado = models.ForeignKey(ProjectMembers, on_delete=models.CASCADE, null=True, blank=True)
    completado = models.BooleanField(default=False)
    project= models.ForeignKey(Project, on_delete=models.CASCADE)
    stage= models.ForeignKey(Stage, on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombre + " || \t || " + self.project.nombre
    
    