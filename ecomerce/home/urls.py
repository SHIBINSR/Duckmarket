from django.urls import path
from . import views


urlpatterns = [
    path('base',views.base,name="Base"),
    path('',views.home,name="Home"),
    path("productview",views.productview,name="Productview"),
    path("filter-category",views.filter_category,name="Filter_category")
]
