from django.forms import ModelForm
from project.models import Project, Task, Comment
from user.models import Profile


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'category',
                  'start_date', 'end_date', 'banner']


class TaskCreationForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'end_date']


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
