"""
This URL configuration file (urls.py) sets up routing for a Django application named blogapp.
It is designed to handle URLs for displaying a list of articles through the ArticleListView.
"""


from django.urls import path
from .views import ArticleListView

app_name = 'blogapp'

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article')
]
