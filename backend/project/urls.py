from django.urls import path, include
from . import api

urlpatterns = [
    path("api/v1/tasks", api.TaskList.as_view(), name="tasks"),
    path('api-auth/', include('rest_framework.urls')),
]
