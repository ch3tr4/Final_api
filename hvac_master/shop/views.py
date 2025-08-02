from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Count 

# Create your views here.

def index(request):
    top_header = TopHeader.objects.all()
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))  
    dataSubMenu = SubMenu.objects.all() 
    dataSub2Menu = Sub2Menu.objects.all() 
    home_banner = HomeBanner.objects.all()
    service = Service.objects.all()
    feature = Feature.objects.all()
    dataCar = Car.objects.all()
    dataImage = CarImage.objects.all()
    choose_us = ChooseUs.objects.all()
    blog = Blog.objects.all()
    blogimage = BlogImage.objects.all()
    footer_section = FooterSection.objects.all()
    context = {
        'top_headers': top_header,
        'dataMenus': dataMenu,
        'dataSubMenus': dataSubMenu,
        'dataSub2Menus': dataSub2Menu,
        'home_banners': home_banner,
        'services': service,
        'features': feature,
        'choose_uss': choose_us,
        'blogs': blog,
        'blogimages': blogimage,
        'dataCars': dataCar,
        'dataImages': dataImage,
        'footer_sections': footer_section,
    }
    return render(request, 'index.html',context)

def about(request):
    top_header = TopHeader.objects.all()
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))  
    dataSubMenu = SubMenu.objects.all() 
    dataSub2Menu = Sub2Menu.objects.all() 
    blog = Blog.objects.all()
    blogimage = BlogImage.objects.all()
    footer_section = FooterSection.objects.all()
    context = {
        'top_headers': top_header
        ,'dataMenus': dataMenu
        ,'dataSubMenus': dataSubMenu
        ,'dataSub2Menus': dataSub2Menu
        ,'blogs': blog
        ,'blogimages': blogimage
        ,'footer_sections': footer_section
    }
    return render(request, 'about.html', context)

def blog_details(request):
    top_header = TopHeader.objects.all()
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))  
    dataSubMenu = SubMenu.objects.all() 
    dataSub2Menu = Sub2Menu.objects.all()
    blog = Blog.objects.all()
    blogimage = BlogImage.objects.all()
    footer_section = FooterSection.objects.all()
    context = {
        'top_headers': top_header
        ,'dataMenus': dataMenu
        ,'dataSubMenus': dataSubMenu
        ,'dataSub2Menus': dataSub2Menu
        ,'blogs': blog
        ,'blogimages': blogimage
        ,'footer_sections': footer_section
    }
    return render(request, 'blog-details.html' , context)

def blog(request):
    top_header = TopHeader.objects.all()
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))
    dataSubMenu = SubMenu.objects.all()
    dataSub2Menu = Sub2Menu.objects.all()
    blog = Blog.objects.all()
    blogimage = BlogImage.objects.all()
    footer_section = FooterSection.objects.all()
    context = {
        'top_headers': top_header
        ,'dataMenus': dataMenu
        ,'dataSubMenus': dataSubMenu
        ,'dataSub2Menus': dataSub2Menu
        ,'blogs': blog
        ,'blogimages': blogimage
        ,'footer_sections': footer_section
    }
    return render(request, 'blog.html'  , context)

def car(request):
    top_header = TopHeader.objects.all()
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))
    dataSubMenu = SubMenu.objects.all()
    dataSub2Menu = Sub2Menu.objects.all()
    dataCar = Car.objects.all()
    dataImage = CarImage.objects.all()
    blog = Blog.objects.all()
    blogimage = BlogImage.objects.all()
    footer_section = FooterSection.objects.all()
    context = {
        'dataCars': dataCar,
        'dataImages': dataImage,
        'top_headers': top_header
        ,'dataMenus': dataMenu
        ,'dataSubMenus': dataSubMenu
        ,'dataSub2Menus': dataSub2Menu
        ,'blogs': blog
        ,'blogimages': blogimage
        ,'footer_sections': footer_section
    }
    return render(request, 'car.html',context)

def car_details(request):
    top_header = TopHeader.objects.all()
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))
    dataSubMenu = SubMenu.objects.all()
    dataSub2Menu = Sub2Menu.objects.all()  
    
    footer_section = FooterSection.objects.all()
    context = {
        'top_headers': top_header
        ,'dataMenus': dataMenu
        ,'dataSubMenus': dataSubMenu
        ,'dataSub2Menus': dataSub2Menu
        ,'footer_sections': footer_section
    }
    return render(request, 'car-details.html', context)

def contact(request):
    top_header = TopHeader.objects.all()
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))
    dataSubMenu = SubMenu.objects.all()
    dataSub2Menu = Sub2Menu.objects.all()
    footer_section = FooterSection.objects.all()
    context = {
        'top_headers': top_header
        ,'dataMenus': dataMenu
        ,'dataSubMenus': dataSubMenu
        ,'dataSub2Menus': dataSub2Menu
        ,'footer_sections': footer_section
    }
    return render(request, 'contact.html', context)

def add_to_cart(request):
    top_header = TopHeader.objects.all()
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))
    dataSubMenu = SubMenu.objects.all()
    dataSub2Menu = Sub2Menu.objects.all()
    footer_section = FooterSection.objects.all()
    context = {
        'top_headers': top_header,
        'dataMenus': dataMenu,
        'dataSubMenus': dataSubMenu,
        'footer_sections': footer_section,
    }   
    return render(request, 'add-to-cart.html', context)

def checkout(request):
    top_header = TopHeader.objects.all()
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))  
    dataSubMenu = SubMenu.objects.all() 
    dataSub2Menu = Sub2Menu.objects.all() 
    footer_section = FooterSection.objects.all()
    context = {
        'top_headers': top_header,
        'footer_sections': footer_section,
        'dataMenus': dataMenu,
        'dataSubMenus': dataSubMenu,
        'dataSub2Menus': dataSub2Menu,
    }
    return render(request, 'checkout.html', context)



