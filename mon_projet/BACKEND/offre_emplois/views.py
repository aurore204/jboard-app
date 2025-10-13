from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
import json

from .models import People, Companies, Annonces, Candidatures
from .serializers import PeopleSerializer, CompaniesSerializer, AnnoncesSerializer, CandidaturesSerializer


# --- API CRUD pour tes modèles ---
class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class CompaniesViewSet(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer


class AnnoncesViewSet(viewsets.ModelViewSet):
    queryset = Annonces.objects.all()
    serializer_class = AnnoncesSerializer


class CandidaturesViewSet(viewsets.ModelViewSet):
    queryset = Candidatures.objects.all()
    serializer_class = CandidaturesSerializer


# --- API LOGIN ---
@csrf_exempt
def login(request):
    if request.method != "POST":
        return JsonResponse({"status": "error", "message": "Requête POST requise"})

    try:
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        # Vérifie dans People
        people = People.objects.filter(email=email).first()
        if people and check_password(password, people.password):
            return JsonResponse({"status": "success", "id": people.id, "role": "people"})

        # Vérifie dans Companies
        companies = Companies.objects.filter(email=email).first()
        if companies and check_password(password, companies.password):
            return JsonResponse({"status": "success", "id": companies.id, "role": "companies"})

        # Vérifie dans Admin (table User de Django)
        admin = User.objects.filter(email=email).first()
        if admin and admin.check_password(password):
            return JsonResponse({"status": "success", "id": admin.id, "role": "admin"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
@csrf_exempt
def register(request):
    if request.method != "POST":
        return JsonResponse({"status": "error", "message": "Requête POST requise"})

    try:
        data = json.loads(request.body)
        role = data.get("role", "people")  # par défaut : people

        # Enregistrement d’un People
        if role == "people":
            if People.objects.filter(email=data["email"]).exists():
                return JsonResponse({"status": "error", "message": "Email déjà utilisé"})
            people = People.objects.create(
                first_name=data.get("first_name", ""),
                last_name=data.get("last_name", ""),
                email=data["email"],
                password=make_password(data["password"]),
                phone=data.get("phone", ""),
                address=data.get("address", ""),
            )
            return JsonResponse({"status": "success", "id": people.id, "role": "people"})

        # Enregistrement d’une Company
        elif role == "companies":
            if Companies.objects.filter(email=data["email"]).exists():
                return JsonResponse({"status": "error", "message": "Email déjà utilisé"})
            companies = Companies.objects.create(
                name=data.get("name", ""),
                email=data["email"],
                password=make_password(data["password"]),
                phone=data.get("phone", ""),
                address=data.get("address", "")
            )
            return JsonResponse({"status": "success", "id": companies.id, "role": "companies"})

        else:
            return JsonResponse({"status": "error", "message": "Rôle invalide"})

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
        return JsonResponse({"status": "error", "message": "Email ou mot de passe incorrect"})