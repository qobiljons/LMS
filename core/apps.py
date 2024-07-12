from django.apps import AppConfig
from django.core.management import call_command
import time

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    label = 'core'

    def ready(self):  
        from django.conf import settings
        if settings.RUN_MIGRATIONS_ON_START:
            time.sleep(20)
            call_command('makemigrations', interactive=False, verbosity=0)
            time.sleep(20)  # Allow database migrations to complete before applying them.
            call_command('migrate', interactive=False, verbosity=0)
