"""
This command is specifically tailored for demonstration or utility purposes within
a development environment due to the hardcoded values.
For production usage, additional modifications such as parameterizing input values
might be necessary to enhance its flexibility and applicability.
"""

from typing import Sequence

from django.contrib.auth.models import User

from django.core.management import BaseCommand

from   shopapp.models import Order

from shopapp.models import Product


class Command(BaseCommand):
    """
    Creating Orders
    """
    def handle(self, *args, **options):
        self.stdout.write("")
        user = User.objects.get(username='project')
        products: Sequence[Product] = Product.objects.defer('delivery_address')

        order,created = Order.objects.get_or_create(
           delivery_address='Hanrapetuyan 22',
           promocode='hello',
            user=user,
    )

        self.stdout.write(f'Created Order: {order}')

