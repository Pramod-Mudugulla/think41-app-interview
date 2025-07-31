import csv
from django.core.management.base import BaseCommand
from products.models import Product, Department
from django.db import transaction

class Command(BaseCommand):
    help = 'Load products from CSV and link to Department model'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        with open('products.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dept_name = row['department'].strip()
                department, _ = Department.objects.get_or_create(name=dept_name)

                Product.objects.create(
                    id=int(row['id']),
                    cost=row['cost'] or 0,
                    category=row['category'],
                    name=row['name'],
                    brand=row['brand'],
                    retail_price=row['retail_price'] or 0,
                    department=department,
                    sku=row['sku'],
                    distribution_center_id=row['distribution_center_id'] or 0
                )

        self.stdout.write(self.style.SUCCESS('Products loaded successfully.'))
