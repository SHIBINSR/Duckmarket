from django.shortcuts import render,HttpResponse,redirect
from . models import  *
from django.http import JsonResponse
import json
from django.template.loader import render_to_string
from django.contrib.auth.models import User

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
    main_category = MainCategory.objects.all()
    category = Category.objects.all()
    product = Products.objects.all()
    
    context = {
        "maincategory":main_category,
        "category":category,
        'products':product
    }
    return render(request,"product-view.html",context)

def filter_category(request):
    product = Products.objects.all()
    is_error = False
    if request.method == 'POST':
        jsondata = json.loads(request.body.decode('utf-8'))
        req = jsondata.get("categories")
        product = Products.objects.filter(category__id__in=req).distinct()
        if len(req) == 0:
            product = Products.objects.all()
        if len(product) == 0:
            is_error = True
        context = {
            'products':product,
            "is_error":is_error
        }
        data = render_to_string("includes/ajax/product_filtered.html",context)

    return JsonResponse({
        "status":"success",
        "data":data,
        "message":"",
    })
          
        
def product_details(request,slug):
    product = Products.objects.get(slug=slug)
    context ={
        'product':product,
        
    }
    return render(request,"product-details.html",context)
     
def about(request):
    main_category = MainCategory.objects.all()
    context = {
        "maincategory":main_category,  
    }
    return render(request,"about.html",context)
         
         
def blog(request):
    main_category = MainCategory.objects.all()
    context = {
        "maincategory":main_category,
    }
    return render(request,"blog.html",context)
      
           
def blog_details(request):
    main_category = MainCategory.objects.all()
    context = {
        "maincategory":main_category, 
    }
    return render(request,"blog-details.html",context)

def my_account(request):
    main_category = MainCategory.objects.all()
    context = {
        "maincategory":main_category,
    }
    return render(request,"my-account.html",context)

def user_validate(request,username,field):
    if field=="username":
        user = User.objects.filter(username=username).exists()
        if user:
            return JsonResponse({
                "status":"error",
                "data":"",
                "message":"username already exists",
            })
        else:
            return JsonResponse({
                "status":"success",
                "data":"",
                "message":"",
            })
    if field=="email":
        user = User.objects.filter(email=username).exists()
        if user:
            return JsonResponse({
                "status":"error",
                "data":"",
                "message":"email is already exists",
            })
        else:
            return JsonResponse({
                "status":"success",
                "data":"",
                "message":"",
            }) 
    if field=="phone":
        user = User_address.objects.filter(phone_number=username).exists()
        if user:
            return JsonResponse({
                "status":"error",
                "data":"",
                "message":"Phone number is already exists",
            })
        else:
            return JsonResponse({
                "status":"success",
                "data":"",
                "message":"",
            })
    return JsonResponse({
        "status":"success",
        "data":"",
        "message":"sd",
    })

def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('userpass')
        
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()

        user_address = User_address(user=user, phone_number=phone, address=address)
        user_address.save()
    
    return redirect("My-account")

def cart(request):
    
    return render(request,"cart.html")