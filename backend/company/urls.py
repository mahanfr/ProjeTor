from django.urls import path
from company.views import company_view

urlpatterns = [
    path('', company_view, name='company-view'),
    path('create/', company_view, name='company-create'),
    path('join/', company_view, name='company-join'),
]
