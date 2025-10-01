from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(name='Машины', descriptions='Категория машин')

        cars = [
            {'name': 'Mercedes', 'description': 'Brand new car', 'category': category, 'price': 5000000},
            {'name': 'BMW', 'description': 'German car', 'category': category, 'price': 3000000},
        ]

        for car_data in cars:
            car, created = Product.objects.get_or_create(**car_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added car: {car.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Car already exists: {car.name}'))
                