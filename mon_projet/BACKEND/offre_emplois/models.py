from django.db import models
from django.contrib.auth.hashers import make_password


class People(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    cv = models.FileField(upload_to='cvs/')
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=128)
    horaire_travail = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
            # Si le mot de passe n'est pas encore haché
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
            super().save(*args, **kwargs)
    class Meta:
        db_table = 'people'  # Nom personnalisé dans la base

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email} - {self.phone} - {self.address} - {self.password}- {self.horaire_travail} - {self.cv.url if self.cv else 'No CV'} - Created at: {self.created_at} - Updated at: {self.updated_at}"


class Companies(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
            super().save(*args, **kwargs)
    class Meta:
        db_table = 'companies'  # Nom personnalisé dans la base
    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone} - {self.address} - {self.password} - Created at: {self.created_at} - Updated at: {self.updated_at}"


class Annonces(models.Model):
    TYPE_CONTRAT_CHOICES = [
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('Stage', 'Stage'),
        ('Freelance', 'Freelance'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)
    type_contrat = models.CharField(max_length=100, choices=TYPE_CONTRAT_CHOICES)
    dateLimite = models.DateField()
    datePublication = models.DateField(auto_now_add=True)
    companies = models.ForeignKey(Companies, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'annonces'  # Nom personnalisé dans la base
    def __str__(self):
        return f"{self.title} - {self.description} - {self.location} - {self.salaire} - Companies: {self.companies.name} - dateLimite: {self.dateLimite} - datePublication: {self.datePublication} - Type de contrat: {self.type_contrat} - Created at: {self.created_at} - Updated at: {self.updated_at}"


class Candidatures(models.Model):
    STATUS_CHOICES = [
        ('En attente', 'En attente'),
        ('Acceptée', 'Acceptée'),
        ('Refusée', 'Refusée'),
    ]

    people = models.ForeignKey(People, on_delete=models.CASCADE)
    annonces = models.ForeignKey(Annonces, on_delete=models.CASCADE)
    dateCandidature = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='En attente')
    emailsent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'candidatures'  # Nom personnalisé dans la base
    def __str__(self):
        return f"People: {self.people.first_name} {self.people.last_name} - Annonce: {self.annonces.title} - Date de candidature: {self.dateCandidature} - Status: {self.status} - Created at: {self.created_at} - Updated at: {self.updated_at}"
