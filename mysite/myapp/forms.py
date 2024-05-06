"""
This module defines two forms, OrderForm and ProductForm,
which are used to collect data about orders and products, respectively.
Both forms inherit from Django's ModelForm, making it efficient to create a form directly from a model.
"""


from django import forms
from .models import Product, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = 'delivery_address','promocode','color'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price","description","color","preview","discount"


