from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from project.models import Project, Task
from company.models import Team
from project.forms import ProjectCreationForm, TaskCreationForm, CommentCreationForm


@login_required(login_url='login')
def project_index(request):
    userCompany = request.user.profile.company
    projects = Project.objects.filter(company=userCompany)
    teams = Team.objects.filter(company=userCompany)
    projectCreationForm = ProjectCreationForm()
    return render(request, 'project/project.html', {'projects': projects, 'teams': teams, 'projectCreationForm': projectCreationForm})


@login_required
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    taskCreationForm = TaskCreationForm()
    if request.user.profile.company != project.company:
        return redirect('project_index')
    tasks = project.task_set.all()
    return render(request, 'project/project_detail.html', {'project': project, 'tasks': tasks, 'taskCreationForm': taskCreationForm})


@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectCreationForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.company = request.user.profile.company
            project.manager = request.user.profile
            project.save()
            return redirect('project_index')
    return redirect('project_index')


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = Project.objects.get(id=request.POST.get('project'))
            task.save()
            return redirect('project_detail', pk=task.project.pk)
    return redirect('project_index')


@login_required
def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    if request.user.profile.company != task.project.company:
        return redirect('project_index')
    comments = task.comments.all()
    commentCreationForm = CommentCreationForm()
    return render(request, 'project/task_detail.html', {'task': task, 'comments': comments, 'commentCreationForm': commentCreationForm})


@login_required
def comment_create(request):
    if request.method == 'POST':
        form = CommentCreationForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = Task.objects.get(id=request.POST.get('task'))
            comment.author = request.user.profile
            comment.save()
            return redirect('task_detail', pk=comment.task.pk)
    return redirect('project_index')
