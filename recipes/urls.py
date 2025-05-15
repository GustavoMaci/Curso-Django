from django.contrib import admin
from django.urls import path
from recipes.views import home, contato, sobre # Adicionado

urlpatterns = [
    path('', home),  # Home
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato),  # /contato/
]