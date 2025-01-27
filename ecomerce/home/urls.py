from django.urls import path
from . import views

urlpatterns = [
    path('base',views.base,name="Base"),
    path('',views.home,name="Home"),
    path("product-view",views.productview,name="Productview"),
    path("filter-category",views.filter_category,name="Filter_category"),
    path("product-details",views.product_details,name="Productdetails")
]