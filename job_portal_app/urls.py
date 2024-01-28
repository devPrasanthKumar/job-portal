
from django.urls import path
from . import views

urlpatterns = [
    path("index", views.IndexView.as_view(), name="index"),
    path("profile/<int:pk>", views.UserProfile.as_view(), name="profile")
]
