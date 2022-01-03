from django.shortcuts import render, redirect
from user.forms import UserRegisterForm
from project.models import Task
from company.models import Company, JoinRequest
# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "user/register.html", {"form": form})


def profile(request):
    company_requests = []
    user_team = request.user.profile.team_set.all()
    projects = request.user.profile.company.project_set.filter(
        team__in=user_team)
    tasks = Task.objects.filter(project__in=projects)
    user_requests = JoinRequest.objects.filter(
        user=request.user)
    if request.user == request.user.profile.company.admin:
        company_requests = JoinRequest.objects.filter(
            company=request.user.profile.company)
    context = {"tasks": tasks,
               "projects": projects,
               "user_requests": user_requests,
               "company_requests": company_requests
               }
    return render(request, "user/profile.html", context=context)
