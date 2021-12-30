from django.forms import ModelForm
from project.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'category',
                  'start_date', 'end_date', 'banner']
