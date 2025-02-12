from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
from django.contrib.auth.models import User

# Create your models here.
class Slider(models.Model):
    Choices = (
        ('New Deal', 'New Deal'),
        ('Hot Deal', 'Hot Deal'),
        ('New arrival', 'New arrival'),
        ('Best seller', 'Best seller')
    )
    title = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to="slider")
    deal = models.CharField(choices=Choices, max_length=200,null=True)
    sale = models.IntegerField()
    discount = models.IntegerField()
    link = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.title


class Banner_area(models.Model):
    sale = (
        ('intelligent','intelligent'),
        ('onsale','onsale'),
        ('hotsale','hotsale')
    )
    title = models.CharField(max_length=200,null=True)
    sale = models.CharField(choices=sale,max_length=200,null=True)
    images = models.ImageField(upload_to="bannerarea")
    discount = models.IntegerField()
    
    def __str__(self):
        return self.title


class MainCategory(models.Model):
    title = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=200,null=True)
    maincategory = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    title = models.CharField(max_length=200,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Products(models.Model):
    title = models.CharField(max_length=200,null =True)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    price = models.PositiveBigIntegerField(default=0,null= True)
    discount = models.PositiveBigIntegerField(default=0,null=True)
    featured_image = models.CharField(max_length=200,null=True)
    total =  models.PositiveBigIntegerField(default=0,null=True)
    available = models.PositiveBigIntegerField(default=0,null=True)
    description = RichTextField(blank=True, null=True,)
    product_information = RichTextField(blank=True,null=True,)
    tags = models.CharField(max_length=200,null=True,blank=True)
    slug = models.CharField(max_length=555, null=True, blank=True)
    brand = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.title



@receiver(pre_save,sender=Products,)
def generate_slug(sender,instance,*args,**kwargs):
    if not instance.slug:
        base_slug = slugify(instance.title)
        unique_slug = base_slug
        while Products.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{base_slug}-{instance.id}"
        instance.slug = unique_slug


class Aditional_information(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True,blank=True)
    spec = models.CharField(max_length=200,null=True,blank=True)

class Aditional_image(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = models.CharField(max_length=550,null=True,blank=True)

class User_address(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(null=True,blank=True)
    