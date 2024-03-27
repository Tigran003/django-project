from django.contrib.auth.models import User

from django.core.management import BaseCommand

from   shopapp.models import Order


class Command(BaseCommand):
    """
    Creating Orders
    """
    def handle(self, *args, **options):
        self.stdout.write("")
        user = User.objects.get(username='project')

        order,created = Order.objects.get_or_create(
           delivery_address='Hanrapetuyan 22',
           promocode='hello',
            user=user,
    )

        self.stdout.write(f'Created Order: {order}')

