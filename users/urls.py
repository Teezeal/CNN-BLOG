from django.urls import path
from .views import api_register_view

urlpatterns = [
    path("register", api_register_view, name="register")
]