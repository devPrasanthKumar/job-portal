from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from .forms import UserRegisterationForm


# views
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, LogoutView


class UserRegisterationView(FormView):
    form_class = UserRegisterationForm
    success_url = reverse_lazy("login")
    template_name = "user/register.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "user/login.html"
    next_page = "index"


class UserLogoutView(LogoutView):
    next_page = "login"
