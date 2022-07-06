from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.index),
    path('homegoods', views.homegoods),
    path('kitchen', views.kitchen),
    path('bathroom', views.bathroom),
    path('electronics', views.electronics),
    path('outdoors', views.outdoors),
    path('cart', views.cart),
    path('products', views.products),
    path('searchpage', views.searchpage),
]
