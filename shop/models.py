from django.db import models

# Create your models here.

class Car(models.Model):

    stock = models.CharField(max_length=200,null=True)
    laste_on_sale = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='cars/', null=True, blank=True)
    vin = models.CharField(max_length=200,null=True)
    originalPrice = models.CharField(max_length=200,null=True)
    price = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=200,null=True)
    year = models.CharField(max_length=200,null=True)
    mile = models.CharField(max_length=200,null=True)
    tranmission = models.CharField(max_length=200,null=True)
    housepw = models.CharField(max_length=200,null=True)
    def __str__(self):
        return f'{self.name} - {self.year}'

class CarImage(models.Model):
    carId = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)

    def __str__(self):
        return f'Image for {self.carId.name} - {self.carId.year}'

class TopHeader(models.Model):
    shift = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    def __str__(self):
        return f'Top Header - {self.shift} | {self.email} | {self.phone}'
    
class FooterSection(models.Model):
    title = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return f'Footer - {self.title} | {self.phone} | {self.email}'

class Feature(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Feature - {self.title}'

class Menu(models.Model):
    MenuNameEN = models.CharField(max_length=200, null=True)
    OrderBy = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return f'{self.id} | {self.MenuNameEN} '

class MenuDetail(models.Model):
    MenuID = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    def __str__(self):         
        return self.MenuID.MenuNameEN
    
class TitleBanner(models.Model):
    MenuID = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True)
    text = models.CharField(max_length=200, null=True)
    def __str__(self):
        return f'{self.title} | {self.text} '

class Menu2(models.Model):
    MenuNameEN = models.CharField(max_length=200, null=True)
    OrderBy = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return f'{self.id} | {self.MenuNameEN} '

class MenuDetail2(models.Model):
    MenuID = models.ForeignKey(Menu2, on_delete=models.CASCADE, null=True)
    def __str__(self):         
        return self.MenuID.MenuNameEN
    
class TitleBanner2(models.Model):
    MenuID = models.ForeignKey(Menu2, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True)
    text = models.CharField(max_length=200, null=True)
    def __str__(self):
        return f'{self.title} | {self.text} '
  