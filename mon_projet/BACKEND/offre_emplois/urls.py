from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PeopleViewSet, CompaniesViewSet, AnnoncesViewSet,CandidaturesViewSet
router = DefaultRouter()
router.register(r'people', PeopleViewSet)
router.register(r'companies', CompaniesViewSet)
router.register(r'annonces', AnnoncesViewSet)
router.register(r'Candidatures', CandidaturesViewSet)
urlpatterns = [
    path('', include(router.urls)),
]