from django.apps import AppConfig


class DemonSoulsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demon_souls'

    def ready(self):
        import demon_souls.signals
