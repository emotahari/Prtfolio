
from django.urls import path

from getdata import views

urlpatterns = [
    path("", views.GetContent, name="get"),
    path("gold", views.GetGold, name="getgold"),
]