from django.urls import path
from .views import SignUpView
from django.contrib.auth import urls, views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]