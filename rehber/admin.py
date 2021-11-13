from django.contrib import admin
from rehber.models import Profil,Rehber


class ProfilAdmin(admin.ModelAdmin):
    list_display = ('id','user','sehir','kendiNo')

class RehberAdmin(admin.ModelAdmin):
    list_display = ('id','user_profil','isim','soyisim', 'telno' )
    
admin.site.register(Profil,ProfilAdmin)
admin.site.register(Rehber,RehberAdmin)