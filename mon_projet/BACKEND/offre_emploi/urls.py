"""
URL configuration for offre_emploi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include  # 👈 ajoute include ici !
from rest_framework.routers import DefaultRouter
from offre_emplois.views import PeopleViewSet, CompaniesViewSet, AnnoncesViewSet,CandidaturesViewSet

router = DefaultRouter()
router.register(r'people', PeopleViewSet)
router.register(r'companies', CompaniesViewSet)
router.register(r'annonces', AnnoncesViewSet)
router.register(r'candidatures', CandidaturesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('offre_emplois.urls')),
]
