from django.http import JsonResponse
import json
from .models import Personne, Entreprise, Annonce, Candidature
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect

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

    
# Liste des Personnes
def personnes_list(request):
    personnes = Personne.objects.all().values(
        'id',
        'nom',
        'prenom',
        'email',
        'cv',
        'created_at',
        'updated_at'
    )
    return JsonResponse(list(personnes), safe=False)


# Liste des Entreprises
def entreprises_list(request):
    entreprises = Entreprise.objects.all().values(
        'id',
        'nom',
        'email',
        'departement',
        'created_at',
        'updated_at'
    )
    return JsonResponse(list(entreprises), safe=False)


# Liste des Annonces
def annonces_list(request):
    annonces = Annonce.objects.all().values(
        'id',
        'intitule_emploi',
        'description',
        'entreprise__nom',
        'departement',
        'salaire',
        'type_contrat',
        'horaires',
        'date_publication',
        'updated_at'
    )
    return JsonResponse(list(annonces), safe=False)


# Liste des Candidatures
def candidatures_list(request):
    candidatures = Candidature.objects.all().values(
        'id',
        'personne__nom',
        'personne__prenom',
        'personne__email',
        'personne__cv',
        'annonce__intitule_emploi',
        'date_candidature',
        'updated_at'
    )
    return JsonResponse(list(candidatures), safe=False)

from django.http import JsonResponse, Http404
from .models import Annonce

def annonces_details_list(request, id):
    try:
        annonce = Annonce.objects.values(
            'id',
            'intitule_emploi',
            'description',
            'entreprise__nom',
            'departement',
            'salaire',
            'type_contrat',
            'horaires',
            'date_publication',
            'updated_at'
        ).get(id=id)
    except Annonce.DoesNotExist:
        raise Http404("Annonce non trouvée")
    
    return JsonResponse(annonce)

def personnes_details_list(request, id):
    try:
        personne = Personne.objects.values(
        'id',
        'nom',
        'email',
        'departement',
        'created_at',
        'updated_at'
        ).get(id=id)
    except Personne.DoesNotExist:
        raise Http404("Personnes non trouvée")
    
    return JsonResponse(personne)

def entreprises_details_list(request, id):
    try:
        entreprise = Entreprise.objects.values(
        'id',
        'nom',
        'email',
        'departement',
        'created_at',
        'updated_at'
        ).get(id=id)
    except Entreprise.DoesNotExist:
        raise Http404("Entreprise non trouvée")
    
    return JsonResponse(entreprise)

