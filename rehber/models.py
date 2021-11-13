from django.db import models
from django.contrib.auth.models import User #db de var olan admin panelde ki user modelini çekiyoruz

class Profil(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profil')
    sehir=models.CharField(max_length=100,blank=True)
    kendiNo=models.CharField(max_length=20,blank=True)
    
    class Meta:
        verbose_name_plural='Profiller'
        
    def __str__(self):
        return self.user.username
    
class Rehber(models.Model):
    user_profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    isim=models.CharField(max_length=50,blank=True)
    soyisim=models.CharField(max_length=50,blank=True)
    dtarih=models.DateField(auto_now=False)
    telno=models.CharField(max_length=20)
    yaratilma_zamani=models.DateTimeField(auto_now_add=True)
    guncelleme_zamani=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural='Numaralar'
        
    def __str__(self):
        return str(self.user_profil)
