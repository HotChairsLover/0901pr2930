from django.urls import path
from auth.views import UserAuth, logout_request

urlpatterns = [
    path('', UserAuth.as_view(), name="user_auth"),
    path("logout", logout_request, name="user_logout"),
]