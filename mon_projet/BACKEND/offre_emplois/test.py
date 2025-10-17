@csrf_exempt # Désactive la vérification CSRF pour cette vue (à utiliser avec précaution) la on pourra utiliser des POST pour des requtes
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


@csrf_exempt# per
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

    mysql -u myuser -p mydatabase

    aushan123