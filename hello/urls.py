from django.urls import path
from . import views

app_name = "hello"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("hello/", views.hello_world_view, name="hello"),
]
