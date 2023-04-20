from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


class UserAuth(LoginView):
    template_name = "auth/login.html"


def logout_request(request):
    logout(request)
    return redirect(reverse("store_items"))