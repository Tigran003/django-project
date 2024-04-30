from django.core.management import BaseCommand

from   shopapp.models import Product


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

