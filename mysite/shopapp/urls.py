from django import views
from django.contrib.auth.views import LoginView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import orders_list, groups_list, shop_index, create_order, ProductsListView, \
    create_products, ProductDetailView, ProductUpdateView, ProductDeleteView, OrderDetailView, OrderUpdateView,HelloView,\
ProductViewSet


app_name = 'shopapp'


router = DefaultRouter()
router.register('products',ProductViewSet)
# router.register('products',ProductViewSet)


urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('api/',include(router.urls)),
    path("", shop_index, name='shop_index'),
    path('groups/', groups_list,name='groups_list'),
    path('create/', create_products, name='create-product'),
    path('orders/', create_order, name='create-order'),
    path('order/', orders_list, name='order-list'),
    # path('products/', products_list, name='products-list'),
    path('products/',ProductsListView.as_view(), name='products-list'),
    path('products/<int:pk>/',ProductDetailView.as_view(), name='product_details'),
    path('products/<int:pk>/update/',ProductUpdateView.as_view(), name='update_product'),
    path('products/<int:pk>/archived/', ProductDeleteView.as_view(), name='delete_product'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='orders_details'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='update_orders'),
    ]





    # path('products/<int:pk>/', ProductDetailsView.as_view(), name='product_details')
