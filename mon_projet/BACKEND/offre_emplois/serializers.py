from rest_framework import serializers
from .models import People, Companies, Annonces,Candidatures

class PeopleSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = People
        fields = '__all__'

class CompaniesSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Companies
        fields = '__all__'

class AnnoncesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annonces
        fields = '__all__'

class CandidaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatures
        fields = '__all__'
