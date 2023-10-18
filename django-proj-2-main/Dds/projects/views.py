from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from projects.models import Project, ProjectMembers, ProjectTask , Stage
from projects.forms import FormCreateProject, FormTaskProject

# Create your views here.

# my_project es la vista donde se muestran los proyectos que tiene el usuario actualmente
# y donde también se le permite crear proyectos

@login_required 
def my_project(request):
    project = Project.objects.filter().order_by('nombre').all()
    member= ProjectMembers.objects.filter(person=request.user)
    f= FormCreateProject()
            
    if request.method == 'GET':
        return render(request, 'project.html',{'form': f, 'project': project, 'member': member})
    
    if request.method == 'POST': 
        try:            
            form = FormCreateProject(request.POST)
            if form.is_valid():
                new_project = form.save(commit=False)
                new_project.admin = request.user
                new_project.save()
                
                stage_1 = Stage.objects.create(nombre="To Do", project=new_project,color="todo")
                stage_2 = Stage.objects.create(nombre="In Progress", project=new_project,color="inprogress")
                stage_3 = Stage.objects.create(nombre="Done", project=new_project, color="done")
            
            return redirect('project')
        
        except ValueError:
                project = Project.objects.filter(admin=request.user).order_by('nombre').all()
                return render(request, 'create_project.html', {
                'form': FormCreateProject,
                'error':'Please provide valid data',
                'project': project
        })
    
    return render(request, 'project.html',{'project':project,'form':FormCreateProject , 'member': member})

#project_view ahora mismo solo muestra la tabla kanban y muestra las tareas que estan creadas para que el usuario las vea
#aun falta incluir que cada proyecto al crearse generé unas etapas que vendrán por defecto las cuales son:
#To Do, In Progress, Done

def project_view(request,project_id):
    stage= Stage.objects.filter(project=project_id)
    task= ProjectTask.objects.filter(project=project_id).order_by('nombre').all()
    member= ProjectMembers.objects.filter(project=project_id)
    project= get_object_or_404(Project, id=project_id)
    
    f= FormTaskProject()
    f.onlyProjectStages(project_id)
    
    if request.method == 'POST':     
        
        try:
            project= get_object_or_404(Project, id=project_id)
            stage= get_object_or_404(Stage, id=request.POST['stage'])
            form = FormTaskProject(request.POST)
            
            if form.is_valid():
                new_task = form.save(commit=False)
                new_task.project = project
                new_task.stage = stage
                new_task.save()
            
            return redirect('project_view',project_id)
        
        except ValueError: 
            stage= Stage.objects.filter(project=project_id)
            project= get_object_or_404(Project, id=project_id)
            task= ProjectTask.objects.filter(project=project_id).order_by('nombre').all()
            member= ProjectMembers.objects.filter(project=project_id)
            
            f= FormTaskProject()
            f.onlyProjectStages(project_id)
            
            return render(request, 'project_view.html', { 'task':task, 'stage':stage, 'form':f,
            'error':'Please provide valid data', 'project': project, 'member':member})
        
        
    return render (request, 'project_view.html',{'task':task, 'stage':stage, 'form':f ,'member':member, 'project':project})

@login_required    
def delete_project_task(request, project_id, task_id):
    task = get_object_or_404(ProjectTask, pk=task_id, project=project_id)
    if request.method == 'POST':
        task.delete()
        print('task deleted successfully')
        return redirect('project_view',project_id)
    