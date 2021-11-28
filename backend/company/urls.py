from django.urls import path
from company.views import company_view, company_create

urlpatterns = [
    path('', company_view, name='company-view'),
    path('create/', company_create, name='company-create'),
    path('join/', company_view, name='company-join'),
]
