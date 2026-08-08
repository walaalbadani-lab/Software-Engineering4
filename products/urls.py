from django.urls import path
from . import views

app_name = "e_invites"

urlpatterns = [
    path("", views.home, name="home"),
]