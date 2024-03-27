from timeit import default_timer

from django.contrib.auth.models import Group, User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Product, Order
from .forms import OrderForm, ProductForm


def shop_index(request: HttpRequest) -> HttpResponse:
    # return HttpResponse('<h1>Hello Shop Index</1>')

    context ={
        'runtime': default_timer()
    }

    return render(request, 'shopapp/index.html', context=context)


def groups_list(request: HttpRequest) -> HttpResponse:
    context = {
        'groups': Group.objects.all()
    }
    return render(request, 'shopapp/groups-list.html', context=context)


def orders_list(request: HttpRequest) -> HttpResponse:
    context = {
        'orders': Order.objects.all()
    }

    return render(request, 'shopapp/order-list.html', context=context)

def products_list(request: HttpRequest) -> HttpResponse:

    context = {
        'products': Product.objects.all()

    }
    return render(request, 'shopapp/product-list.html', context=context)


def create_products(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            Product.objects.create(name=name, price=price)
    else:
        form = ProductForm()

    context = {
    'form' : form

    }
    return render(request, 'shopapp/create-product.html', context=context)


def create_order(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            # form.instance.user = request.user.id
            # form.save()
            user_instance = User.objects.get(id=1)
            delivery_address = form.cleaned_data['delivery_address']
            promocode = form.cleaned_data['promocode']
            color = form.cleaned_data['color']
            order_instance = Order.objects.create(delivery_address=delivery_address, promocode=promocode, color=color , user =user_instance )
    else:
        form = OrderForm()

    context = {
        'form': form
    }

    return render(request, 'shopapp/create-order.html', context=context)