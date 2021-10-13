from django.shortcuts import render, HttpResponse
from .models import products

# Create your views here.
def index(request):
  product_objects = products.objects.all()
  return render(request, 'index.html',{'product_objects': product_objects})
