from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    top_header = TopHeader.objects.all()
    dataCar = Car.objects.all()
    dataImage = CarImage.objects.all()
    feature = Feature.objects.all()
    footer_section = FooterSection.objects.all()
    context = {
        'dataCars': dataCar,
        'dataImages': dataImage,
        'top_headers': top_header,
        'features': feature,
        'footer_sections': footer_section
    }
    return render(request, 'index.html',context)

def about(request):
    top_header = TopHeader.objects.all()
    footer_section = FooterSection.objects.all()
    context = {
        'top_headers': top_header
        ,'footer_sections': footer_section
    }
    return render(request, 'about.html', context)

def blog_details(request):
    top_header = TopHeader.objects.all()
    footer_section = FooterSection.objects.all()
    context = {
        'top_headers': top_header
        ,'footer_sections': footer_section
    }
    return render(request, 'blog-details.html' , context)

def blog(request):
    top_header = TopHeader.objects.all()
    footer_section = FooterSection.objects.all()
    context = {
        'top_headers': top_header
        ,'footer_sections': footer_section
    }
    return render(request, 'blog.html'  , context)

def car(request):
    top_header = TopHeader.objects.all()
    dataCar = Car.objects.all()
    dataImage = CarImage.objects.all()
    footer_section = FooterSection.objects.all()
    context = {
        'dataCars': dataCar,
        'dataImages': dataImage,
        'top_headers': top_header
        ,'footer_sections': footer_section
    }
    return render(request, 'car.html',context)

def car_details(request):
    top_header = TopHeader.objects.all()
    footer_section = FooterSection.objects.all()
    context = {
        'top_headers': top_header
        ,'footer_sections': footer_section
    }
    return render(request, 'car-details.html', context)

def contact(request):
    top_header = TopHeader.objects.all()
    footer_section = FooterSection.objects.all()
    context = {
        'top_headers': top_header
        ,'footer_sections': footer_section
    }
    return render(request, 'contact.html', context)

def add_to_cart(request):
    top_header = TopHeader.objects.all()
    footer_section = FooterSection.objects.all()
    context = {
        'top_headers': top_header
        ,'footer_sections': footer_section
    }   
    return render(request, 'add-to-cart.html', context)

def checkout(request):
    top_header = TopHeader.objects.all()
    footer_section = FooterSection.objects.all()
    context = {
        'top_headers': top_header
        ,'footer_sections': footer_section
    }
    return render(request, 'checkout.html', context)



