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
    menu = Menu.objects.all()
    menu2 = Menu2.objects.all()

    context = {
        'dataCars': dataCar,
        'dataImages': dataImage,
        'top_headers': top_header,
        'features': feature,
        'footer_sections': footer_section,
        'menus' : menu,
        'menus2' : menu2,
    }
    return render(request, 'index.html',context)

def MenuDetailMethod(request, pk):
    title_banner = TitleBanner.objects.filter(MenuID = pk)
    text_banner = TitleBanner.objects.filter(MenuID = pk)
    top_header = TopHeader.objects.all()
    dataCar = Car.objects.all()
    dataImage = CarImage.objects.all()
    feature = Feature.objects.all()
    footer_section = FooterSection.objects.all()
    menu = Menu.objects.all()
    menu_detail = MenuDetail.objects.filter(MenuID = pk)
    menu2 = Menu2.objects.all()
    menu_detail2 = MenuDetail2.objects.filter(MenuID = pk)

    context = {
        'title_banners' : title_banner,
        'text_banners' : text_banner,
        'dataCars': dataCar,
        'dataImages': dataImage,
        'top_headers': top_header,
        'features': feature,
        'footer_sections': footer_section,
        'menus' : menu,
        'menu_details' : menu_detail,
        'menus2' : menu2,
        'menu_details2' : menu_detail2,
    }
    return render(request, 'menu-details.html',context)

def MenuDetailMethod2(request, pk):
    title_banner = TitleBanner2.objects.filter(MenuID = pk)
    text_banner = TitleBanner2.objects.filter(MenuID = pk)
    top_header = TopHeader.objects.all()
    dataCar = Car.objects.all()
    dataImage = CarImage.objects.all()
    feature = Feature.objects.all()
    footer_section = FooterSection.objects.all()
    menu = Menu.objects.all()
    menu_detail = MenuDetail.objects.filter(MenuID = pk)
    menu2 = Menu2.objects.all()
    menu_detail2 = MenuDetail2.objects.filter(MenuID = pk)

    context = {
        'title_banners' : title_banner,
        'text_banners' : text_banner,
        'dataCars': dataCar,
        'dataImages': dataImage,
        'top_headers': top_header,
        'features': feature,
        'footer_sections': footer_section,
        'menus' : menu,
        'menu_details' : menu_detail,
        'menus2' : menu2,
        'menu_details2' : menu_detail2,
    }
    return render(request, 'menu-details2.html',context)

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
    menu = Menu.objects.all()
    menu2 = Menu2.objects.all()
    context = {
        'top_headers': top_header,
        'footer_sections': footer_section,
        'menus' : menu,
        'menus2' : menu2,
    }   
    return render(request, 'add-to-cart.html', context)

def checkout(request):
    top_header = TopHeader.objects.all()
    footer_section = FooterSection.objects.all()
    menu = Menu.objects.all()
    menu2 = Menu2.objects.all()
    context = {
        'top_headers': top_header,
        'footer_sections': footer_section,
        'menus' : menu,
        'menus2' : menu2,
    }
    return render(request, 'checkout.html', context)



