from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Create and apply migrations on start'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating migrations...')
        call_command('makemigrations')
        self.stdout.write('Applying migrations...')
        call_command('migrate')
        self.stdout.write(self.style.SUCCESS('Migrations created and applied successfully.'))
