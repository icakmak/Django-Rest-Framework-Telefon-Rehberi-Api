from rehber.models import Profil, Rehber
from rest_framework import serializers

class ProfilSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Profil
        fields = '__all__'
        
        
class RehberSerializer(serializers.ModelSerializer):
    user_profile = serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Rehber
        # fields = '__all__'
        exclude=['user_profil','yaratilma_zamani','guncelleme_zamani']
    
        