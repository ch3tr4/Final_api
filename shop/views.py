from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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

def blog_details(request, pk):
    top_header = TopHeader.objects.all()
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))  
    dataSubMenu = SubMenu.objects.all() 
    dataSub2Menu = Sub2Menu.objects.all()
    blog = Blog.objects.all()
    blogdetail = BlogDetails.objects.filter(blogId = pk)
    blogimage = BlogImage.objects.all()
    footer_section = FooterSection.objects.all()
    context = {
        'top_headers': top_header
        ,'dataMenus': dataMenu
        ,'dataSubMenus': dataSubMenu
        ,'dataSub2Menus': dataSub2Menu
        ,'blogs': blog
        ,'blogdetails': blogdetail
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

def car_details(request, id):
    top_header = TopHeader.objects.all()
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))
    dataSubMenu = SubMenu.objects.all()
    dataSub2Menu = Sub2Menu.objects.all()
    cardetail = CarDetails.objects.filter(carId = id)
    cardetailimage = CarDetailImage.objects.filter(carId = id)
    footer_section = FooterSection.objects.all()
    context = {
        'top_headers': top_header
        ,'dataMenus': dataMenu
        ,'dataSubMenus': dataSubMenu
        ,'dataSub2Menus': dataSub2Menu
        ,'cardetails': cardetail
        ,'cardetailimages': cardetailimage
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

# def add_to_cart(request):
#     top_header = TopHeader.objects.all()
#     dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))
#     dataSubMenu = SubMenu.objects.all()
#     dataSub2Menu = Sub2Menu.objects.all()
#     footer_section = FooterSection.objects.all()
#     context = {
#         'top_headers': top_header,
#         'dataMenus': dataMenu,
#         'dataSubMenus': dataSubMenu,
#         'footer_sections': footer_section,
#     }   
#     return render(request, 'add-to-cart.html', context)

def checkout(request):
    top_header = TopHeader.objects.all()
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))  
    dataSubMenu = SubMenu.objects.all() 
    dataSub2Menu = Sub2Menu.objects.all() 
    footer_section = FooterSection.objects.all()
    # Get cart data from session
    cart = request.session.get('cart', {})
    cart_clean = {k: v for k, v in cart.items() if isinstance(v, dict)}
    for item in cart_clean.values():
        item['quantity'] = int(item.get('quantity', 1))
        item['price'] = float(item.get('price', 0))
        item['subtotal'] = item['price'] * item['quantity']
    total_price = sum(item['subtotal'] for item in cart_clean.values())
    context = {
        'top_headers': top_header,
        'footer_sections': footer_section,
        'dataMenus': dataMenu,
        'dataSubMenus': dataSubMenu,
        'dataSub2Menus': dataSub2Menu,
        'cart_items': cart_clean.items(),
        'total_price': total_price
    }
    return render(request, 'checkout.html', context)


from rest_framework import generics
from .serializers import ProductSerializer

# Create your views here.

# ListCreateAPIView provides GET (list) and POST (create) actions
class CarsListCreate(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = ProductSerializer

# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions

class CarsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = ProductSerializer


# add-to-cart
from django.shortcuts import render, redirect, get_object_or_404

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    key = str(product_id)
    # Ensure cart[key] is a dict before updating
    if key in cart and isinstance(cart[key], dict):
        cart[key]['quantity'] += 1
    else:
        product = CarDetails.objects.get(id=product_id)
        # Try to get image from product, else from CarDetailImage, else use default
        image_url = ''
        # Check for image field and its value
        if hasattr(product, 'image') and getattr(product, 'image'):
            try:
                image_url = product.image.url
            except Exception:
                image_url = ''
        # If still no image, try CarDetailImage
        if not image_url:
            image_obj = CarDetailImage.objects.filter(carId=product.carId).first()
            if image_obj and hasattr(image_obj, 'image') and getattr(image_obj, 'image'):
                try:
                    image_url = image_obj.image.url
                except Exception:
                    image_url = ''
        # Fallback to default image
        if not image_url:
            image_url = '/static/img/no-image.png'
        price_str = str(product.price).replace(',', '')
        cart[key] = {
            'name': product.name,
            'price': float(price_str),
            'quantity': 1,
            'image': image_url
        }
    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    top_header = TopHeader.objects.all()
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))
    dataSubMenu = SubMenu.objects.all()
    dataSub2Menu = Sub2Menu.objects.all()
    footer_section = FooterSection.objects.all()
    cart = request.session.get('cart', {})
    # Filter out any non-dict values
    cart_clean = {k: v for k, v in cart.items() if isinstance(v, dict)}
    # Ensure correct types and add subtotal
    for item in cart_clean.values():
        item['quantity'] = int(item.get('quantity', 1))
        item['price'] = float(item.get('price', 0))
        item['subtotal'] = item['price'] * item['quantity']
    total_price = sum(item['subtotal'] for item in cart_clean.values())
    context = {
        'top_headers': top_header,
        'dataMenus': dataMenu,
        'dataSubMenus': dataSubMenu,
        'dataSub2Menus': dataSub2Menu,
        'footer_sections': footer_section,
        'cart_items': cart_clean.items(),
        'total_price': total_price
    }
    return render(request, 'add-to-cart.html', context)

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('view_cart')


def ProtectedAPI(request):
    token = request.GET.get('token')
    if not token:
        return JsonResponse({'error': 'Token is required'}, status=400)

    if not AccessToken.objects.filter(token=token, is_active=True).exists():
        return JsonResponse({'error': 'Invalid or inactive token'}, status=403)
    
    # Query all items
    cars = Car.objects.all().values('id', 'name', 'year', 'image', 'price', 'stock')
    return JsonResponse({'cars': list(cars)})
