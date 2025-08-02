from django.contrib import admin
from .models import *

class AdminMenu(admin.ModelAdmin):
    list_display = [
        'menuName', 
    ] 
    list_filter = [
        'menuName', 
    ] 
    search_fields = [
        'menuName', 
    ] 
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="1. Menu " 

class AdminSubMenu(admin.ModelAdmin):
    list_display = [
        'menuName', 
    ] 
    list_filter = [
        'menuName', 
    ] 
    search_fields = [
        'menuName', 
    ] 
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="1. Sub Menu  " 

admin.site.register(TopHeader)
admin.site.register(Menu,AdminMenu) 
admin.site.register(SubMenu,AdminSubMenu) 
admin.site.register(Sub2Menu)
admin.site.register(HomeBanner)
admin.site.register(Service)
admin.site.register(Feature)
admin.site.register(Car)
admin.site.register(CarImage)
admin.site.register(ChooseUs)
admin.site.register(LastestBlog)
admin.site.register(FooterSection)

# admin.site.register(TitleBanner)
# admin.site.register(TitleBanner2)


