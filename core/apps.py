from django.apps import AppConfig
from django.core.management import call_command

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    label = "core"

    def ready(self):
        from django.conf import settings
        if settings.RUN_MIGRATIONS_ON_START:
            call_command('migrate')
