from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from .models import Personne, Entreprise, Annonce, Candidature
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect
from rest_framework import viewsets
from .serializers import PersonneSerializer, EntrepriseSerializer, AnnonceSerializer, CandidatureSerializer, AnnonceReduiteSerializer

@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")
            type_user = data.get("type")  # "personne" ou "entreprise"

            if type_user == "personne":
                from .models import Personne
                user = Personne.objects.get(email=email)
            elif type_user == "entreprise":
                from .models import Entreprise
                user = Entreprise.objects.get(email=email)
            else:
                return JsonResponse({"success": False, "error": "Type d'utilisateur invalide"})

            if check_password(password, user.mot_de_passe):
                return JsonResponse({"success": True, "id": user.id, "type": type_user})
            else:
                return JsonResponse({"success": False, "error": "Mot de passe incorrect"})
        except (Personne.DoesNotExist, Entreprise.DoesNotExist):
            return JsonResponse({"success": False, "error": "Utilisateur non trouvé"})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    return JsonResponse({"success": False, "error": "Méthode non autorisée"})



@csrf_exempt
def create_entreprise(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            entreprise = Entreprise.objects.create(
                nom=data["nom"],
                email=data["email"],
                departement=data.get("departement", ""),
                mot_de_passe=make_password(data["mot_de_passe"])
            )
            return JsonResponse({"message": "Entreprise créée avec succès", "id": entreprise.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

@csrf_exempt
def create_personnes(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            personne = Personne.objects.create(
                nom=data["nom"],
                email=data["email"],
                mot_de_passe=make_password(data["mot_de_passe"])
            )
            return JsonResponse({"message": "Compte Utilisateur créée avec succès", "id": personne.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

class PersonneViewSet(viewsets.ModelViewSet):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer

class EntrepriseViewSet(viewsets.ModelViewSet):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer

class AnnonceViewSet(viewsets.ModelViewSet):
    queryset = Annonce.objects.all()
    serializer_class = AnnonceSerializer  # par défaut

    def perform_create(self, serializer):
        # On récupère l'entreprise depuis le localStorage via le payload JS
        entreprise_id = self.request.data.get('entreprise')
        entreprise = Entreprise.objects.get(id=entreprise_id)
        serializer.save(entreprise=entreprise)

    def get_serializer_class(self):
        entreprise_id = self.request.GET.get('entreprise_id')
        if self.action == 'list' and not entreprise_id:
            # Liste générale → réduite
            return AnnonceReduiteSerializer
        # Sinon → complète
        return AnnonceSerializer

    def get_queryset(self):
        entreprise_id = self.request.GET.get('entreprise_id')
        if entreprise_id:
            return Annonce.objects.filter(entreprise_id=entreprise_id)
        return Annonce.objects.all()


class CandidatureViewSet(viewsets.ModelViewSet):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
@api_view(['GET'])
def liste_candidat_annonces(request, annonce_id):
    try:
        candidatures = Candidature.objects.filter(annonce_id=annonce_id)
        serializer = CandidatureSerializer(candidatures, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
@api_view(['GET'])
def status_options(request):
    try:
        options = ["En attente", "Accepté", "Refusé"]
        return JsonResponse(options, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['PATCH'])
def update_candidature_status(request, candidature_id):
    try:
        data = json.loads(request.body)
        status = data.get("status")

        if not status:
            return JsonResponse({'error': 'Statut manquant'}, status=400)

        print("Updating candidature ID:", candidature_id, "to status:", status)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)