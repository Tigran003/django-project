"""
This Python script is a Django management command part of a Django project named shopapp.
The script's primary function is to perform bulk updates on a Product model by applying
a discount to all products that include "Smartphone" in their name.
Additionally, the script is structured to demonstrate the use of Django's bulk operations
but primarily focuses on updating records for this example.
"""


from django.core.management import BaseCommand
from shopapp.models import Product

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Start demo Bulk actions')

        result = Product.objects.filter(
            name__contains='Smartphone'
        ).update(discount=20)
        print(result)

        # info = [
        #     ('Smartphone 5', 1999),
        #     ('Smartphone 6', 2999),
        #     ('Smartphone 7', 3999),
        # ]
        #
        # products = [
        #     Product(name=name, price=price)
        #     for name, price in info
        # ]
        #
        # result = Product.objects.bulk_create(products)
        # for obj in result:
        #     print(obj)

        self.stdout.write('End demo Bulk actions')