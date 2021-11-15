from django.contrib import admin
from django.urls import path

# we need to import views from our contact app
from Ecom import views

urlpatterns = [
  path('', views.index, name='index'),
  path('furn', views.furnitures, name='furniture'),
  path('elec', views.electronics, name='electronics'),
  path('car', views.automobiles, name='automobiles')
]
