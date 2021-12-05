from django.urls import path, include
from . import api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('project', api.ProjectViewSet)
router.register('project', api.TaskViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
]
