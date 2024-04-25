from django.urls import path
from .views import hello_world_view, GroupListView, ProductListView
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView

app_name = 'myapiapp'



urlpatterns = [
    path('hello/', hello_world_view, name='hello'),
    path('groups/', GroupListView.as_view(), name='groups'),
    path('products/', ProductListView.as_view(), name='products'),
    path('api/schema/swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),


]


