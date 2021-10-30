from django.urls import path
from landing.views import index_view

urlpatterns = [
    path('', index_view, name='index'),
]
