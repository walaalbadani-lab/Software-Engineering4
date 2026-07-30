from django.urls import path
from . import views


app_name = "e_invites"


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("order/", views.order, name="order"),
]