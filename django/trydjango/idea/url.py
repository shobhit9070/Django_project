from django.urls import path

from . import views

urlpatterns = [
    path('', views.what_to_start, name='index'),
]