from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core import validators
from .models import Product, Order


# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     price = forms.DecimalField(min_value=1, max_value=100000)
#     description = forms.CharField(
#         label='Product description',
#         widget=forms.Textarea(attrs={"rows": 5, "cols": '33'}),
#         validators=[validators.RegexValidator(
#             regex=r'great',
#             message='Field must contain word great'
#         )],
#     )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = 'delivery_address','promocode','color'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price","description","color","preview"



