from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import  *
from django.http import JsonResponse
import json
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def base(request):
    return render(request,"base.html")
     
def home(request):
    main_category = MainCategory.objects.all()
    banner_area = Banner_area.objects.all()
    slider = Slider.objects.all()
    product = Products.objects.all()
    cart =  Cart.objects.all()
    
    context = {
        'slider':slider,
        "banner_area":banner_area,
        "maincategory":main_category,
        'products':product,
        "cart":cart
    }
     
    return render(request,"home.html",context)

def productview(request):
    main_category = MainCategory.objects.all()
    category = Category.objects.all()
    product = Products.objects.all()
    cart =  Cart.objects.all()
    context = {
        "maincategory":main_category,
        "category":category,
        'products':product,
        "cart":cart
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
    main_category = MainCategory.objects.all()
    product = Products.objects.get(slug=slug)
    cart =  Cart.objects.all()
    context ={
        'product':product,
        "cart":cart,
        "maincategory":main_category,  # for breadcrumbs  # add breadcrumbs in your template with {{ maincategory }}  # and {{ product.category }}  # or {{ product.category.parent }}  # and so on.  # and {{ product.category.parent.parent }}  # and so on.  # and so on.  # and so on.  # and so on.  # and so on.  # and so on.
    }
    return render(request,"product-details.html",context)
     
def about(request):
    main_category = MainCategory.objects.all()
    cart =  Cart.objects.all()
    context = {
        "maincategory":main_category,  
        "cart":cart,
    }
    return render(request,"about.html",context)
                 
def blog(request):
    cart =  Cart.objects.all()
    main_category = MainCategory.objects.all()
    context = {
        "maincategory":main_category,
        "cart":cart,
    }
    return render(request,"blog.html",context)
         
def blog_details(request):
    main_category = MainCategory.objects.all()
    cart =  Cart.objects.all()
    context = {
        "maincategory":main_category, 
        "cart":cart,
    }
    return render(request,"blog-details.html",context)

def my_account(request):
    main_category = MainCategory.objects.all()
    cart =  Cart.objects.all()
    context = {
        "maincategory":main_category,
        "cart":cart,
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
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            messages.success(request, "Login successfully.")
            login(request,user)
            return redirect("Home")
        # messages.success(request, 'Registration successful')
    
    return redirect("Home")

def Login(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("pass")
        print(username,password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            messages.success(request, "Login successfully.")
            login(request,user)
            return redirect("Home")
        else:
            messages.warning(request, "Invalid credentials Try again.")
            return redirect("Login") 
    return render(request,"my-account.html")

def Logout(request):
    logout(request)
    messages.success(request, "Logout successfully.")
    return redirect("Home")
        
def cart(request):
    main_category = MainCategory.objects.all()
    cart = Cart.objects.all()
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
    else:
        session_id = request.session.session_key
        if not session_id:
            request.session.create()
        cart_items = Cart.objects.filter(session_id=request.session.session_key)

    total_amount = sum(item.total_price() for item in cart_items)

    return render(request, "cart.html", {"cart_items": cart_items, "total_amount": total_amount,"cart":cart,"maincategory":main_category})

def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.user.is_authenticated:
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    else:
        session_id = request.session.session_key
        if not session_id:
            request.session.create()
        cart_item, created = Cart.objects.get_or_create(session_id=request.session.session_key, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
     
    return redirect('Cart')
def update_cart(request, cart_id, action):
    cart_item = get_object_or_404(Cart, id=cart_id)

    if action == "increase":
        cart_item.quantity += 1
    elif action == "decrease" and cart_item.quantity > 1:
        cart_item.quantity -= 1

    cart_item.save()
    return redirect('Cart')

def remove_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.delete()
    return redirect('Cart')

def wishlist(request):
    return render(request,"wishlist.html")