from django.shortcuts import render, HttpResponse
from .models import products

# Create your views here.
def index(request):
  product_objects = products.objects.filter(category='grocery')
  return render(request, 'index.html',{'product_objects': product_objects})

def electronics(request):
     product_objects= products.objects.filter(category='electronics')
     return render(request, 'electronic.html',{'product_objects': product_objects})

def furnitures(request):
     product_objects= products.objects.filter(category='furnitures')
     return render(request, 'furniture.html',{'product_objects': product_objects})

def automobiles(request):
     product_objects= products.objects.filter(category='automobiles')
     return render(request, 'car.html',{'product_objects': product_objects})
