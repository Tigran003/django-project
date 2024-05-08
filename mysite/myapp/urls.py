"""
This documentation describes the URL configuration for a Django application named ShopApp.
The configuration handles URL routing, linking URLs to specific views,
and is designed for an e-commerce or shopping application context
"""


from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import groups_list, shop_index, create_order, ProductsListView, \
    ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView, OrderDetailView, OrderUpdateView, \
    HelloView, \
    ProductViewSet, OrdersListView, ProductsDataExportView

app_name = 'myapp'


router = DefaultRouter()
router.register('products',ProductViewSet)


urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('api/',include(router.urls)),
    path("", shop_index, name='shop_index'),
    path('groups/', groups_list,name='groups_list'),
    path('orders/', create_order, name='create-order'),
    path('order/',OrdersListView.as_view(),name='order-list'),
    path('products/',ProductsListView.as_view(), name='products-list'),
    path('create/',ProductCreateView.as_view(), name='create-product'),
    path('products/export/', ProductsDataExportView.as_view(), name='products-export'),
    path('products/<int:pk>/',ProductDetailView.as_view(), name='product_details'),
    path('products/<int:pk>/update/',ProductUpdateView.as_view(), name='update_product'),
    path('products/<int:pk>/archived/', ProductDeleteView.as_view(), name='delete_product'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='orders_details'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='update_orders'),
    ]





