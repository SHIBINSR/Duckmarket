from django.contrib import admin
from . models import *


class SubCategoryTabular(admin.TabularInline):
    model = SubCategory

class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryTabular]



class AditionalinfoTabular(admin.TabularInline):
    model = Aditional_information

class AditionalimgTabular(admin.TabularInline):
    model = Aditional_image

class ProductsAdmin(admin.ModelAdmin):
    inlines = [AditionalinfoTabular, AditionalimgTabular]


# Register your models here.
admin.site.register(Slider)
admin.site.register(Banner_area)
admin.site.register(MainCategory)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(User_address)
