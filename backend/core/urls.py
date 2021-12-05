from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from project import api as project_api
from company import api as company_api

router = DefaultRouter()
router.register('project/projects', project_api.ProjectViewSet, 'projects')
router.register('project/tasks', project_api.TaskViewSet, 'tasks')
router.register('company/companies', company_api.CompanyViewSet, 'companies')
router.register('company/teams', company_api.TeamViewSet, 'teams')
router.register('company/positions', company_api.PositionViewSet, 'positions')
router.register('company/joinrequests',
                company_api.JoinRequestViewSet, 'joinrequests')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('user/', include('user.urls')),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('company/', include('company.urls')),
    path('projects/', include('project.urls'))
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
