from django.db.models.query import QuerySet
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rehber.models import Profil,Rehber
from rehber.api.serializers import ProfilSerializer,RehberSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rehber.api.permissions import KendiProfiliYadaReadOnly,DurumSahibiYadaReadOnly

class ProfilViewSet(mixins.ListModelMixin, #Listeleme
                    mixins.RetrieveModelMixin, #Detay Görüntüleme
                    mixins.UpdateModelMixin, #güncelleme
                    GenericViewSet
                    ):
    queryset=Profil.objects.all()
    serializer_class=ProfilSerializer
    permission_classes=[IsAuthenticated,KendiProfiliYadaReadOnly]
    

class RehberViewSet(ModelViewSet):
    serializer_class=RehberSerializer
    permission_classes=[IsAuthenticated,DurumSahibiYadaReadOnly]
    filter_backends=[SearchFilter]
    search_fields=['isim','soyisim','telno']
    
    def get_queryset(self):
        queryset=Rehber.objects.all()
        username=self.request.query_params.get('username',None)
        if username is not None:
            queryset=queryset.filter(user_profil__user__username=username)
        return queryset

    def perform_create(self, serializer):
        user_profil=self.request.user.profil
        serializer.save(user_profil=user_profil)
    
