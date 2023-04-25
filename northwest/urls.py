from django.urls import path
from . import views

urlpatterns = [
    path("", views.say_hello, name="index"),
    path("search/", views.search, name="search"),
    path("depart/", views.search, name="depart"),
    path("return/", views.search, name="return"),
]
