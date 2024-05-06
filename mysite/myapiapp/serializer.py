"""
This module defines serializers for the Group and Product models using Django REST Framework.
Serializers allow complex data such as querysets and model instances to be converted to native
Python datatypes that can then be easily rendered into JSON, XML or other content types.
"""
#
# #
from django.contrib.auth.models import Group
from rest_framework import serializers
from  myapp.models import Product

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = 'pk', 'name'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'pk', 'name', 'description', 'color', 'price', 'preview'