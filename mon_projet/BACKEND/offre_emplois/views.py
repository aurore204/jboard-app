from django.shortcuts import render
from rest_framework import viewsets
from .models import People, Companies, Annonces,Candidatures
from .serializers import PeopleSerializer, CompaniesSerializer, AnnoncesSerializer,CandidaturesSerializer

# Create your views here.
class PeopleViewSet(viewsets.ModelViewSet):# ici la class PeopleViewSet hérite de viewsets.ModelViewSet
    queryset = People.objects.all()# on récupère tous les objets People
    serializer_class = PeopleSerializer# on utilise le serializer PeopleSerializer pour convertir les objets People en JSON et vice versa
    # ModelViewSet fournit des actions par défaut pour gérer les opérations CRUD (Create, Read, Update, Delete)
    #queryset et serializer_class sont des attributs essentiels pour configurer le ViewSet.
    #ViewSet est une abstraction puissante dans Django REST Framework qui permet de regrouper la logique de vue pour un ensemble de ressources.
class CompaniesViewSet(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer

class AnnoncesViewSet(viewsets.ModelViewSet):
    queryset = Annonces.objects.all()
    serializer_class = AnnoncesSerializer

class CandidaturesViewSet(viewsets.ModelViewSet):
    queryset = Candidatures.objects.all()
    serializer_class = CandidaturesSerializer
