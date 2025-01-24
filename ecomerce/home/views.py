from django.shortcuts import render,HttpResponse
from . models import  *

# Create your views here.
def base(request):
    return render(request,"base.html")
     

def home(request):
    main_category = MainCategory.objects.all()
    banner_area = Banner_area.objects.all()
    slider = Slider.objects.all()
    product = Products.objects.all()
    
    context = {
        'slider':slider,
        "banner_area":banner_area,
        "maincategory":main_category,
        'products':product
    }
     
    return render(request,"home.html",context)

def productview(request):
    category = Category.objects.all()
    product = Products.objects.all()
    
    context = {
        "category":category,
        'products':product
    }
    return render(request,"product-view.html",context)

def filter_category(request):
    pass
 
