from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    dataCar = Car.objects.all()
    dataImage = CarImage.objects.all()
    context = {
        'dataCars': dataCar,
        'dataImages': dataImage
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def car(request):
    dataCar = Car.objects.all()
    dataImage = CarImage.objects.all()
    context = {
        'dataCars': dataCar,
        'dataImages': dataImage
    }
    return render(request, 'car.html',context)

def car_details(request):
    return render(request, 'car-details.html')

def contact(request):
    return render(request, 'contact.html')

def add_to_cart(request):
    return render(request, 'add-to-cart.html')

def checkout(request):
    return render(request, 'checkout.html')


