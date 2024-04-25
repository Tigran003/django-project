from django.shortcuts import render

from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.views import APIView

from .serializer import GroupSerializer,ProductSerializer
from  shopapp.models import Product


@api_view()
def hello_world_view(request: Request) ->Response:
    return Response({"message":'Hello World!'})

class GroupListView(APIView):
    def get(self,request: Request) -> Response:
        groups = Group.objects.all()
        serialized = GroupSerializer(groups, many=True)
        return Response({'groups':serialized.data})

class ProductListView(APIView):
    def get(self,request : Request) -> Response:
        products = Product.objects.all()
        serialized = ProductSerializer(products, many=True)
        return Response({'products':serialized.data})