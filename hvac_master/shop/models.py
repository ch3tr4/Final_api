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