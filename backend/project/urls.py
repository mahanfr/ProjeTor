from django.urls import path, include
from project.views import project_index, project_detail, project_create, task_create, task_detail, comment_create

urlpatterns = [
    path('', project_index, name='project_index'),
    path('<int:pk>', project_detail, name='project_detail'),
    path('create', project_create, name='project_create'),
    path("task/create", task_create, name="task_create"),
    path('task/<int:pk>', task_detail, name='task_detail'),
    path('comment/create', comment_create, name='comment_create'),
]
