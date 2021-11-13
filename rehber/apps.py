from django.apps import AppConfig


class RehberConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rehber'

    def ready(self): #profil hazır olduğunda burası çalışacak
        import rehber.signals
