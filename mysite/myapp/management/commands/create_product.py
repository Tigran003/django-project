"""
This Django management command, defined in a custom script,
is used to automatically populate the database with a set of predefined products.
Each product is added with a specified name and price if it does not already exist in the database.
The command is implemented in a Django project and utilizes Django's ORM to interact with the database.
"""

from django.core.management import BaseCommand

from   myapp.models import Product


class Command(BaseCommand):
    """
    Create product:
    """

    def handle(self, *args, **options):
        self.stdout.write('Create Product')

        products = [
            'Laptop',
            'Smartphone',
            'Desktop'
        ]

        prices = [
            1999,
            2999,
            999
        ]

        for products,price in zip(products,prices):

            name,created = Product.objects.all().get_or_create(name=products, price=price)
            self.stdout.write(f'Create product: {name} for  ${price}')
        self.stdout.write(self.style.SUCCESS('Products Created'))
