from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView
from .models import Profile
from django.shortcuts import render, get_object_or_404, redirect


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:about_me')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user= self.object)
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password1')
        user = authenticate(self.request,username=username, password=password)
        login(request=self.request, user=user)
        return redirect("accounts:about_me")

    def login_view(request:HttpRequest) -> HttpResponse:
        if request.method == 'GET':
            if request.user.is_authenticated:
                return redirect('/admin/')
        return render(request, 'accounts/login.html')

        username = request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return render(request, 'accounts/login.html')



def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse("accounts:login"))


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password has changed succesfuly')
            return redirect('accounts:login')
    else:
        form= PasswordChangeForm(user=request.user)
    return render(request, 'accounts/change_password.html',{'form':form})


class AboutMeView(TemplateView):
    template_name = "accounts/about_me.html"


class ResetPasswordView(PasswordResetView):
    template_name = "accounts/password_reset_email.html"
    form_class = PasswordResetForm

    def get_success_url(self):
        return reverse_lazy('reset_password_done')



class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"


class PasswordResetConfirmViewCustom(PasswordResetConfirmView):
    template_name = "accounts/password_reset_form.html"
    success_url = ("password_reset_complete"),


class PasswordResetCompleteViewCustom(PasswordResetCompleteView):
    template_name = "accounts/password_reset_sent.html"