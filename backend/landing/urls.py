from django.urls import path
from landing.views import index_view, pricing_view, support_view, about_view

urlpatterns = [
    path('', index_view, name='index'),
    path('pricing', pricing_view, name='pricing'),
    path('support', support_view, name='support'),
    path('about', about_view, name='about'),
]
