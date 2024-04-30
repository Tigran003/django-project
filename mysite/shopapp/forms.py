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



