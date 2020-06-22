from django.core.management.base import BaseCommand, CommandError
from main.models import Client


class Command(BaseCommand):

    def handle(self, *args, **options):
        Client.objects.all().delete()
        print('Load client')
        c = Client()
        c.name = 'wezom'
        c.secret = '123'
        c.save()