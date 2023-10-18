from django.contrib import admin
from projects.models import Project, ProjectMembers, Stage , ProjectTask

# Register your models here.
class ProjectoAdmin(admin.ModelAdmin):
    readonly_fields = ("fechaInicio",)

admin.site.register(Project, ProjectoAdmin)
admin.site.register(ProjectMembers)
admin.site.register(ProjectTask)
admin.site.register(Stage)