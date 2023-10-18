"""Dds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from projects import views as vP


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #home and login paths
    path('',views.home, name='home'),
    path('signup/',views.signup, name="signup"),
    path('login/',views.loguserin, name="login"),
    path('logout/',views.loguserout, name="logout"),
    
    #Task (user) paths
    path('menu/',views.menu, name="menu"),
    path('tasks/',views.task, name="usertask"),
    path('tasks/<int:task_id>/complete',views.complete_task, name="complete_task"),
    path('tasks/<int:task_id>/delete',views.delete_task, name="delete_task"),
    
    #Project (user) paths
    path('project/',vP.my_project, name="project"),
    path('project/view/<int:project_id>',vP.project_view, name="project_view"),
    path('project/view/<int:project_id>/<int:task_id>/',vP.delete_project_task, name="project_delete_task"),
]
