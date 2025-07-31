import csv
from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Load products from CSV into the database'

    def handle(self, *args, **kwargs):
        with open('products.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    product, created = Product.objects.get_or_create(
                        id=int(row['id']),
                        defaults={
                            'cost': float(row['cost']),
                            'category': row['category'],
                            'name': row['name'],
                            'brand': row['brand'],
                            'retail_price': float(row['retail_price']),
                            'department': row['department'],
                            'sku': row['sku'],
                            'distribution_center_id': int(row['distribution_center_id']),
                        }
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Created: {product.name}"))
                    else:
                        self.stdout.write(f"Skipped existing: {product.name}")
                except Exception as e:
                    self.stderr.write(f"Error loading product ID {row['id']}: {e}")
