from django.urls import path

from .views import products_list,orders_list,create_products,groups_list,shop_index,create_order

app_name = 'shopapp'

urlpatterns = [
    path('', shop_index, name='shop_index'),
    path('groups/', groups_list,name='groups_list'),
    path('create/', create_products, name='create-product'),
    path('orders/', create_order, name='create-order'),
    path('orders/', orders_list, name='order-list'),
    path('products/', products_list, name='products-list')
]