from django.core.management.base import BaseCommand
from core.models import Ocupacion

class Command(BaseCommand):
    help = 'Cargar ocupaciones iniciales'

    def handle(self, *args, **kwargs):
        ocupaciones = ['Storytelling', 'Business', 'Creative', 'Design', 'Modeling', 'Fashion', 'Acting', 'Influencer', 'Education']
        for ocupacion in ocupaciones:
            Ocupacion.objects.get_or_create(nombre=ocupacion)
        self.stdout.write(self.style.SUCCESS('Ocupaciones iniciales cargadas correctamente.'))
