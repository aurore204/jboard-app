# JBoard - Plateforme de gestion d'offres d'emploi

> Application web fullstack permettant aux entreprises de publier des offres d'emploi et aux candidats de postuler directement en ligne.

---

## Description

JBoard est une plateforme web complète de mise en relation entre **entreprises** et **candidats**. Les entreprises peuvent créer et gérer leurs annonces, tandis que les candidats peuvent parcourir les offres et soumettre leurs candidatures. Un espace administrateur permet de superviser l'ensemble de la plateforme.

---

## Fonctionnalités

### Côté Candidat
- Création et gestion de compte personnel
- Consultation et recherche d'offres d'emploi
- Dépôt de candidature en ligne
- Suivi de ses candidatures

### Côté Entreprise
- Création et gestion de compte entreprise
- Publication et gestion des annonces
- Consultation des candidatures reçues
- Gestion du profil entreprise

### Côté Administrateur
- Supervision complète de la plateforme
- Gestion des utilisateurs (candidats & entreprises)
- Modération des annonces
- Accès au panneau d'administration Django

---

## Stack Technique

| Couche | Technologie |
|--------|------------|
| Backend | Python 3.x, Django, Django REST Framework |
| Frontend | HTML5, CSS3, JavaScript |
| Base de données | MySQL / SQLite |
| Versioning | Git, GitHub |

---

## Structure du projet

```
jboard/
├── BACKEND/
│   ├── offre_emploi/           # Configuration principale Django
│   │   ├── settings.py         # Paramètres de l'application
│   │   ├── urls.py             # Routes principales
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── offre_emplois/          # Application principale
│   │   ├── models.py           # Modèles de données
│   │   ├── views.py            # Logique métier
│   │   ├── serializers.py      # Sérialisation API REST
│   │   ├── urls.py             # Routes de l'application
│   │   ├── admin.py            # Configuration admin
│   │   ├── migrations/         # Migrations base de données
│   │   └── tests.py            # Tests unitaires
│   ├── db.sqlite3              # Base de données SQLite (dev)
│   └── manage.py               # Commandes Django
├── FRONTEND/
│   ├── template/               # Pages HTML
│   │   ├── index.html
│   │   ├── annonces.html
│   │   ├── detail.html
│   │   ├── postuler.html
│   │   ├── Candidatures.html
│   │   ├── compte_utilisateur.html
│   │   ├── compte_entreprise.html
│   │   ├── compte_admin.html
│   │   ├── LoginRegister.html
│   │   └── admin.html
│   ├── css/                    # Feuilles de style
│   ├── js/                     # Scripts JavaScript
│   └── assets/                 # Images et ressources
├── .gitignore
└── README.md
```

---

## Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- MySQL (production) ou SQLite (développement)
- Git

---

## Installation & Lancement

### 1. Cloner le projet

```bash
git clone https://github.com/aurore204/jboard-web-app.git
cd jboard-web-app
```

### 2. Créer un environnement virtuel

```bash
python -m venv env
```

Activer l'environnement virtuel :

- Linux / macOS :
```bash
source env/bin/activate
```
- Windows :
```bash
env\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install mysqlclient        # Si vous utilisez MySQL
pip install python-dotenv      # Pour les variables d'environnement
```

Ou si un fichier `requirements.txt` est disponible :
```bash
pip install -r requirements.txt
```

### 4. Configurer la base de données

#### Option A — SQLite (développement, configuration par défaut)
Aucune configuration supplémentaire requise.

#### Option B — MySQL (production)

Dans `BACKEND/offre_emploi/settings.py`, modifiez la section `DATABASES` :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jboard_db',
        'USER': 'ton_user',
        'PASSWORD': 'ton_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Appliquer les migrations

```bash
cd BACKEND
python manage.py makemigrations
python manage.py migrate
```

### 6. Créer un compte administrateur

```bash
python manage.py createsuperuser
```

Suivez les instructions pour définir un nom d'utilisateur, un email et un mot de passe.

### 7. Lancer le serveur de développement

```bash
python manage.py runserver
```

### 8. Accéder à l'application

| Interface | URL |
|-----------|-----|
| Application | http://127.0.0.1:8000 |
| Panel Admin Django | http://127.0.0.1:8000/admin |
| API REST | http://127.0.0.1:8000/api/ |

---

## Rôles & Permissions

| Rôle | Permissions |
|------|------------|
| Administrateur | Accès complet, gestion des utilisateurs et des annonces |
| Entreprise | Création et gestion de ses propres annonces, consultation des candidatures |
| Candidat | Consultation des annonces, dépôt et suivi de candidatures |

---

## Tests

Pour lancer les tests unitaires :

```bash
cd BACKEND
python manage.py test
```

---

## Commandes utiles

### Vider la base de données
```bash
python manage.py flush
```

### Créer un fichier requirements.txt
```bash
pip freeze > requirements.txt
```

### Ouvrir le shell Django
```bash
python manage.py shell
```

---

## Dépannage

### Erreur de migration
```bash
python manage.py migrate --run-syncdb
```

### Port déjà utilisé
```bash
python manage.py runserver 8080
```

### Problème de connexion MySQL
Vérifiez que le service MySQL est bien démarré et que les identifiants dans `settings.py` sont corrects.

---

## Ressources

- [Documentation Django](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Documentation MySQL](https://dev.mysql.com/doc/)

---

## Auteur

**[Ton Prénom Nom]** — Etudiante en Pré-MSc à Epitech Paris  
[LinkedIn](https://linkedin.com/in/aurore-njimegne) 

---

> Ce projet a été réalisé dans le cadre de la formation Pré-MSc à Epitech Paris.