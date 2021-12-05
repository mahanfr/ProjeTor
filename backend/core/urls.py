from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from project import api as project_api

router = DefaultRouter()
router.register('project/projects', project_api.ProjectViewSet, 'projects')
router.register('project/tasks', project_api.TaskViewSet, 'tasks')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('user/', include('user.urls')),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
