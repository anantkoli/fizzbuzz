from django.urls import path
from . import views

urlpatterns = [
    path("get_fizz_buzz/", views.get_fizz_buzz_resp),
    path("get_stats/", views.get_stats),
]
