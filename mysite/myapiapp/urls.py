"""

This code snippet is part of a Django web application and is responsible
for defining URL patterns specific to an app called myapiapp.
It helps map the URLs to their corresponding view functions or classes in the application.
"""


from django.urls import path
from .views import hello_world_view, GroupListView

#
app_name = 'myapiapp'



urlpatterns = [
    path('hello/', hello_world_view, name='hello'),
    path('groups/', GroupListView.as_view(), name='groups'),


]


