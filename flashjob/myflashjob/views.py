from django.http import JsonResponse
from .models import Personne, Entreprise, Annonce, Candidature

# Liste des Personnes
def personnes_list(request):
    personnes = Personne.objects.all().values(
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
        'personne__nom',
        'personne__prenom',
        'personne__email',
        'personne__cv',
        'annonce__intitule_emploi',
        'date_candidature',
        'updated_at'
    )
    return JsonResponse(list(candidatures), safe=False)
