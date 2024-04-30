from django.contrib.auth.views import LoginView, PasswordResetConfirmView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.urls import path

from .views import RegisterView, logout_view, change_password, AboutMeView
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path("login/",
         LoginView.as_view(
             template_name="accounts/login.html",
             redirect_authenticated_user=True
         ),
         name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/',logout_view,name='logout'),
    path('changepassword',change_password,name='changePassword'),
    path("about_me/", AboutMeView.as_view(), name='about_me'),
    path('reset_password/',PasswordResetView.as_view(),name='reset_password'),
    path('reset_password/done/',PasswordResetDoneView.as_view(),name='reset_password_done'),
    path('reset_password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    ]
