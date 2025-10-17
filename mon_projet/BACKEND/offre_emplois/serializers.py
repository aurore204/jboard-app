from rest_framework import serializers
from .models import Personne, Entreprise, Annonce, Candidature

class PersonneSerializer(serializers.ModelSerializer):
    mot_de_passe = serializers.CharField(write_only=True)

    class Meta:
        model = Personne
        fields = '__all__'


class EntrepriseSerializer(serializers.ModelSerializer):
    mot_de_passe = serializers.CharField(write_only=True)

    class Meta:
        model = Entreprise
        fields = '__all__'

class AnnonceReduiteSerializer(serializers.ModelSerializer):
    entreprise = serializers.SerializerMethodField()  # Au lieu de StringRelatedField

    class Meta:
        model = Annonce
        fields = ['id', 'intitule_emploi', 'entreprise', 'departement', 'type_contrat']

    def get_entreprise(self, obj):
        if obj.entreprise:
            return obj.entreprise.nom  # Affiche juste le nom
        return None

class AnnonceSerializer(serializers.ModelSerializer):
        entreprise = serializers.PrimaryKeyRelatedField(
            queryset=Entreprise.objects.all()
        )
        class Meta:
            model = Annonce
            fields = '__all__'


class CandidatureSerializer(serializers.ModelSerializer):
    personne = serializers.StringRelatedField(read_only=True)
    personne_id = serializers.PrimaryKeyRelatedField(
        queryset=Personne.objects.all(),
        source='personne',
        write_only=True
    )
    annonce = serializers.StringRelatedField(read_only=True)
    annonce_id = serializers.PrimaryKeyRelatedField(
        queryset=Annonce.objects.all(),
        source='annonce',
        write_only=True
    )

    class Meta:
        model = Candidature
        fields = [
            'id', 'personne', 'personne_id',
            'annonce', 'annonce_id',
            'date_candidature', 'updated_at'
        ]
    read_only_fields = ['date_candidature', 'updated_at', 'personne', 'annonce']