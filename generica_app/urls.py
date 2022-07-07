from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.index),
    path('kitchen', views.kitchen),
    path('bed_and_bath', views.bed_and_bath),
    path('electronics', views.electronics),
    path('outdoors', views.outdoors),
    path('cart', views.cart),
    path('products', views.products),
    path('searchpage', views.searchpage),
    # path('add_to_cart', views.add_to_cart),
]
