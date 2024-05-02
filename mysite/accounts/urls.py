"""
This configuration file manages user authentication and account management related paths,
such as login, logout, registration, password change, and password reset functionalities.

-'login/ ': This view handles user authentication. If the user is already authenticated and attempts to access this page, they are redirected to a predefined page.
-'register/':This view handles new user registration, allowing users to create a new account.
-'logout/':This function-based view handles the logout process. When invoked, it terminates the user's session and can redirect the user to another page, typically the homepage or login page.
-'changepassword':This view allows authenticated users to change their password. It typically requires the user to provide the current password and a new password.
-'about_me/:This view displays information about the user, typically accessed from the user's profile. This is a class-based view, possibly rendering a template that includes user-specific data.
"""



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
