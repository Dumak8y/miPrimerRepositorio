from django import forms
from projects.models import Project, ProjectTask, Stage, ProjectMembers

class FormCreateProject(forms.ModelForm):
    class Meta:
        model=Project
        fields=['nombre','descripcion','fechaTermino']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control ','placeholder':'write a name',}),
            'descripcion':forms.Textarea(attrs={'class':'form-control ','placeholder':'write some description','rows':'2'}),
            'fechaTermino':forms.DateInput(attrs={'class':'form-control','type':'date'})
        }
        
class FormTaskProject(forms.ModelForm):
    class Meta:
        model=ProjectTask
        fields=['nombre','descripcion','fechaInicio','fechaTermino','stage','encargado']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control ','placeholder':'write a name',}),
            'descripcion':forms.Textarea(attrs={'class':'form-control ','placeholder':'write some description','rows':'2'}),
            'fechaInicio':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'fechaTermino':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'stage':forms.Select(attrs={'class':'form-control'}),
            'encargado':forms.Select(attrs={'class':'form-control'})
        }
        

    def onlyProjectStages(self, user=None, **kwargs):
        self.fields['stage'].queryset = Stage.objects.filter(project=user)
        self.fields['encargado'].queryset = ProjectMembers.objects.filter(project=user)    
        