
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'personnes', views.PersonneViewSet)
router.register(r'entreprises', views.EntrepriseViewSet)
router.register(r'annonces', views.AnnonceViewSet,basename='annonces')
router.register(r'candidatures', views.CandidatureViewSet)


urlpatterns = [

    path('api/entreprises/create/', views.create_entreprise, name='create_entreprise'),
    path('api/personnes/create/', views.create_personnes, name='create_personnes'),
    path('api/login/', views.login, name='login'),
    path('api/candidatures/<int:annonce_id>/personne/', views.liste_candidat_annonces, name='liste_candidat_annonces'),
    path('api/candidatures/status/', views.status_options, name='status_options'),


    path('api/', include(router.urls)),
]
