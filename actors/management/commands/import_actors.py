import csv
import datetime

from typing import Any
from django.core.management.base import BaseCommand
from actors.models import Actor


class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument(
            'filename',
            type=str,
            help='Nome do arquivo CSV com atores',
        )
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        # comando: python manage.py import_actors
        # python manage.py import_actors filename='teste'
        filename = options['filename']
        # print(f"meu comando, filename: {filename}")
        with open(filename, mode= 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                birthday = datetime.datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                nationality = row['nationality']
                
                self.stdout.write(self.style.NOTICE(f"nome: {name}"))
                
                Actor.objects.create(
                    name=name,
                    birthday=birthday,
                    nationality=nationality,
                )
                
        self.stdout.write(self.style.SUCCESS("Atores importados com sucesso!"))