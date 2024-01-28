from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic import FormView, UpdateView
from .models import UserProfileModel
from job_portal_auth.forms import UserProfileForm


class IndexView(TemplateView):
    template_name = "main/index.html"


class UserProfile(UpdateView):
    model = UserProfileModel
    form_class = UserProfileForm
    success_url = reverse_lazy("index")
    template_name = "user/profile.html"
    pk_url_kwarg = "pk"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
