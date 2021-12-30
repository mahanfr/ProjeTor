from django.urls import path, include
from project.views import project_index, project_detail, project_create

urlpatterns = [
    path('', project_index, name='project_index'),
    path('<int:pk>', project_detail, name='project_detail'),
    path('create', project_create, name='project_create'),
]
