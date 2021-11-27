from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from .serializers import TaskSerializer
from .models import Task
from rest_framework.exceptions import NotAuthenticated
from user.models import User


class TaskList(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            raise NotAuthenticated("You need to Login")
        else:
            # we should optimize the query this is 1:50 AM code
            user_team = self.request.user.profile.team_set.all()
            projects = self.request.user.profile.company.project_set.filter(
                team__in=user_team)
            return Task.objects.filter(project__in=projects)
