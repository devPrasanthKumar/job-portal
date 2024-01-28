from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from job_portal_app.models import UserProfileModel


class UserRegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email",
                  "phone_number", "password1", "password2"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = "__all__"
