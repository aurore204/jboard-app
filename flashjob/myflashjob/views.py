from django.http import JsonResponse
from .models import Personne, Entreprise, Annonce, Candidature

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

