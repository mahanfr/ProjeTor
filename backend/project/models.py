from django.db import models
from django.utils import timezone
from . import enums
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(
        'project.Category', on_delete=models.SET_NULL, null=True, blank=True)
    team = models.ManyToManyField("company.Team", blank=True)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)
    state = models.CharField(
        max_length=100, choices=enums.ProjectState.choices, default=enums.ProjectState.WORKING)
    banner = models.ImageField(
        upload_to='project_banner/', blank=True, null=True, default='default.jpg')
    manager = models.ForeignKey(
        'user.Profile', on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()

    def getTeams(self):
        return self.team.all()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    project = models.ForeignKey(
        'project.Project', on_delete=models.CASCADE)
    state = models.CharField(
        max_length=100, choices=enums.TaskState.choices, default=enums.TaskState.TODO)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    assigned_to = models.ForeignKey(
        'user.Profile', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey(
        'project.Task', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        'user.Profile', on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField(max_length=500)
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body
