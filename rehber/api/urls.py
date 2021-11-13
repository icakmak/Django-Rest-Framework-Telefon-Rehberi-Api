from django.urls import path,include
from rehber.api.views import ProfilViewSet,RehberViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'profiller',ProfilViewSet)
router.register(r'rehber',RehberViewSet,basename='rehber')

urlpatterns =[
    path('',include(router.urls)),
]