from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from project.models import Project
from company.models import Team
from project.forms import ProjectCreationForm


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
    if request.user.profile.company != project.company:
        return redirect('project_index')
    tasks = project.task_set.all()
    return render(request, 'project/project_detail.html', {'project': project, 'tasks': tasks})


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
