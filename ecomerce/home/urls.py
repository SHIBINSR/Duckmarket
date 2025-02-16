from django.urls import path
from . import views

urlpatterns = [
    path('base',views.base,name="Base"),
    path('',views.home,name="Home"),
    path("product-view",views.productview,name="Productview"),
    path("filter-category",views.filter_category,name="Filter_category"),
    path("product/<str:slug>",views.product_details,name="Productdetails"),
    path("about",views.about,name="About"),
    path("blog",views.blog,name="Blog"),
    path("blog-details",views.blog_details,name='Blog-details'),
    path("my-account",views.my_account,name="My-account"),
    path("user-validate/<username>/<field>",views.user_validate,name="User-validate"),
    path("registration",views.registration,name="Registration"),
    path("cart",views.cart,name="Cart"),
    path("login",views.Login,name="Login"),
    path("logout",views.Logout,name="Logout"),
]