from django.urls import path
from .views import base, home, about

urlpatterns = [
    path('base/', base, name='base'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),

]
    