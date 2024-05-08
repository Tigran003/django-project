"""
This Python module defines various views and components for a Django web application,
centered around managing products and orders.
It leverages Django’s class-based views and REST framework capabilities for efficient development
"""

import logging
from timeit import default_timer
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group, User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, request, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, View, UpdateView, DeleteView, DetailView, CreateView
from django.utils.translation import gettext_lazy as _, ngettext
from .models import Product, Order
from .forms import OrderForm, ProductForm
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from myapiapp.serializer import ProductSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse


logger = logging.getLogger(__name__)



class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields = ["name", "description",]
    filterset_fields = [
        "name",
        "description",
        "price",
        "discount",

    ]
    ordering_fields = [
        "name",
        "price",
        "discount",
    ]

    @extend_schema(
        summary='Get one product by ID',
        description='Retrieves **product**, returns 404 if not found',
        responses={
            200: ProductSerializer,
            404: OpenApiResponse(description='Empty response, product by id not found'),
        }
    )
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)


def shop_index(request: HttpRequest) -> HttpResponse:
    # return HttpResponse('<h1>Hello Shop Index</1>')

    context ={
        'runtime': default_timer()
    }

    return render(request, 'myapp/index.html', context=context)


def groups_list(request: HttpRequest) -> HttpResponse:
    context = {
        'groups': Group.objects.all()
    }
    return render(request, 'myapp/groups-list.html', context=context)



class ProductDetailView(View):
    def get(self,request:HttpRequest,pk: int) -> HttpResponse:
        # product = Product.objects.get(pk=pk)
        product = get_object_or_404(Product,pk=pk)
        context = {
            'product': product,
        }
        return render(request, 'myapp/products_details.html', context=context)


class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ["myapp.view_order",]
    queryset = (
        Order.objects
        .select_related('user')
        .prefetch_related('products')
    )


class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    fields = 'name','description','price','discount',"preview"
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse(
            'myapp:product_details',
            kwargs={'pk': self.object.pk},
        )


class OrderUpdateView(LoginRequiredMixin,UpdateView):
    model = Order
    form_class = OrderForm
    template_name_suffix = '_update_'

    def get_success_url(self):
        return reverse(
            'myapp:orders_details',
            kwargs={'pk': self.object.pk},
        )


class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    success_url = reverse_lazy('myapp:products-list')

    def form_valid(self,form):
        success_url = self.get_success_url()
        self.object.archived =True
        self.object.save()
        return HttpResponseRedirect(success_url)


class ProductsListView(ListView):
    template_name = 'myapp/product-list.html'
    model = Product
    context_object_name = 'products'


class OrdersListView(LoginRequiredMixin,ListView):
    template_name = 'myapp/order-list.html'
    model = Order
    context_object_name = 'order'



class ProductCreateView(LoginRequiredMixin, CreateView):
    def test_func(self):
        # return self.request.user.groups.filter(name='secret-group').exists()
        return self.request.user.is_superuser

    model = Product
    fields = "name", "price", "description", "discount", "preview"
    # form_class = ProductForm
    success_url = reverse_lazy("myapp:products-list")


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

    return render(request, 'myapp/create-order.html', context=context)


class HelloView(View):
    welcome_message = _("welcome hello world")

    def get(self, request: HttpRequest) -> HttpResponse:

        items_str = request.GET.get('items') or 0
        items = int(items_str)
        products_line = ngettext(
            "one product",
            "{count} products",
            items,
        )
        products_line = products_line.format(count=items)
        return HttpResponse(
            f"<h1>{self.welcome_message}</h1>"
            f"\n<h2>{products_line}</h2>"

        )

class ProductsDataExportView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        products = Product.objects.order_by("pk").all()
        products_data = [
            {
                "pk": product.pk,
                "name": product.name,
                "price": product.price,
                "is_archived": product.is_archived,
            }
            for product in products
        ]
        elem = products_data[0]
        name = elem['name']
        print(name)
        return JsonResponse({"products": products_data})