from django.urls import path
from . import views

urlpatterns = [
    path('api/personnes/', views.personnes_list, name='personnes_list'),
    path('api/entreprises/', views.entreprises_list, name='entreprises_list'),
    path('api/entreprises/create/', views.create_entreprise, name='create_entreprise'),
    path('api/personnes/create/', views.create_personnes, name='create_personnes'),
    path('api/annonces/', views.annonces_list, name='annonces_list'),
    path('api/candidatures/', views.candidatures_list, name='candidatures_list'),
    path('api/annonces/<int:id>/', views.annonces_details_list, name='annonces_details'),
    path('api/personnes/<int:id>/', views.personnes_details_list, name='personnes_details_list'),
    path('api/entreprises/<int:id>/', views.entreprises_details_list, name='entreprises_details_list'),
    path('api/login/', views.login, name='login'),
]
