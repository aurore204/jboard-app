from django.urls import path
from . import views

urlpatterns = [
    path('api/personnes/', views.personnes_list, name='personnes_list'),
    path('api/entreprises/', views.entreprises_list, name='entreprises_list'),
    path('api/annonces/', views.annonces_list, name='annonces_list'),
    path('api/candidatures/', views.candidatures_list, name='candidatures_list'),
    path('api/annonces/<int:id>', views.annonces_details_list, name='annonces_list'),
]
