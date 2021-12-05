from rest_framework.viewsets import ModelViewSet
from .serializers import TeamSerializer, CompanySerializer, PositionSerializer, JoinRequestSerializer
from .models import Team, Company, Position, JoinRequest
from rest_framework.exceptions import NotAuthenticated


class TeamViewSet(ModelViewSet):
    serializer_class = TeamSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            raise NotAuthenticated("You need to Login")
        else:
            return Team.objects.all()


class PositionViewSet(ModelViewSet):
    serializer_class = PositionSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            raise NotAuthenticated("You need to Login")
        else:
            # we should optimize the query this is 1:50 AM code
            return Position.objects.all()


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            raise NotAuthenticated("You need to Login")
        else:
            return Company.objects.all()


class JoinRequestViewSet(ModelViewSet):
    serializer_class = JoinRequestSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            raise NotAuthenticated("You need to Login")
        else:
            return JoinRequest.objects.all()
