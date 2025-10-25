from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from catalog.models import Product

class Command(BaseCommand):
    help = "Создает группу 'Модератор продуктов' и назначает нужные права"

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name="Модератор продуктов")

        unpublish_perm = Permission.objects.get(codename="can_unpublish_product")
        delete_perm = Permission.objects.get(codename="delete_product")

        group.permissions.set([unpublish_perm, delete_perm])
        group.save()

        if created:
            self.stdout.write(self.style.SUCCESS("Группа 'Модератор продуктов' создана."))
        else:
            self.stdout.write(self.style.WARNING("Группа 'Модератор продуктов' уже существует."))

        self.stdout.write(self.style.SUCCESS("Права успешно назначены."))