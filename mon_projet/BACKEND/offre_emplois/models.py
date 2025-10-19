from django.db import models

# Modèle Personne
class Personne(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cv = models.FileField(upload_to='cvs/')
    mot_de_passe = models.CharField(max_length=128)  # pour stocker un hash de mot de passe
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


# Modèle Entreprise
class Entreprise(models.Model):
    nom = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    departement = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


# Modèle Annonce
class Annonce(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    intitule_emploi = models.CharField(max_length=200)
    description = models.TextField()
    departement = models.CharField(max_length=100)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)
    type_contrat = models.CharField(max_length=50)
    horaires = models.CharField(max_length=100)
    date_publication = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.intitule_emploi} - {self.entreprise.nom}"


# Modèle Candidature
class Candidature(models.Model):
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('en_attente', 'En attente'), ('acceptee', 'Acceptée'), ('refusee', 'Refusée')],default='en_attente')
    date_candidature = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Candidature de {self.personne.prenom} {self.personne.nom} pour {self.annonce.intitule_emploi} pour la date {self.date_candidature} pour status {self.status}"