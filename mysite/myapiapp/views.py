"""
Below is the documentation for the provided Django/DRF code, which defines an API endpoint
and a class-based view to interact with Group model instances.
This code defines a simple API using Django and Django Rest Framework (DRF). It includes:

"""


from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializer import GroupSerializer,ProductSerializer


@api_view()
def hello_world_view(request: Request) ->Response:
    return Response({"message":'Hello World!'})

class GroupListView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer