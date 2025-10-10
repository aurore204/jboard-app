from django.urls import path
from . import views

urlpatterns = [
    path('api/jobs/', views.jobs_list, name='jobs_list'),
]
