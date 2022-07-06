from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import requests as HTTP_Client
from dotenv import load_dotenv
import json
import os
import pprint
# from .models

electronics_list = [
    {
        'id': 1,
        'title': 'Computer',
        'description': 'Surf the Net with Ease!',
        'price': '1800.00',
        'img_url': 'static/assets/laptop.jpeg'
    },
    {
        'id': 2,
        'title': 'Video Game Console',
        'description': 'Adventure Awaits',
        'price': '600.00',
        'img_url': 'static/assets/xbox.jpeg'
    },
    {
        'id': 3,
        'title': 'Television',
        'description': 'Stream your favorite shows right to your home',
        'price': '800.00',
        'img_url': 'static/assets/tv.jpeg'
    },
    {
        'id': 4,
        'title': 'Stereo',
        'description': 'Get the party started',
        'price': '400.00',
        'img_url': 'static/assets/stereo.jpeg'
    },
]

outdoors_list = [
    {
        'id': 1,
        'title': 'Tent',
        'description': 'Spend a night sleeping under the stars',
        'price': '300.00',
        'img_url': 'static/assets/tent.jpeg'
    },
    {
        'id': 2,
        'title': 'Grill',
        'description': 'Charcaol not included',
        'price': '450.00',
        'img_url': 'static/assets/grill.webp'
    },
    {
        'id': 3,
        'title': 'Canoe',
        'description': 'Check out a new kind of Streaming',
        'price': '750.00',
        'img_url': 'static/assets/canoe.jpeg'
    },
    {
        'id': 4,
        'title': 'Bicycle',
        'description': 'Eco-friendly Transportation powered by YOU',
        'price': '1200.00',
        'img_url': 'static/assets/bicycle.jpeg'
    },
]

bed_and_bath_list = [
    {
        'id': 1,
        'title': 'Bed',
        'description': 'Spend a third of your life in comfort',
        'price': '2400.00',
        'img_url': 'static/assets/bed.jpeg'
    },
    {
        'id': 2,
        'title': 'Toilet',
        'description': 'A porcelin throne fit for a king',
        'price': '150.00',
        'img_url': 'static/assets/toilet.jpeg'
    },
    {
        'id': 3,
        'title': 'Dresser',
        'description': 'Wardrobe storage at an affordable price',
        'price': '280.00',
        'img_url': 'static/assets/dresser.jpeg'
    },
    {
        'id': 4,
        'title': 'Shower',
        'description': 'Wake up feeling refreshed',
        'price': '120.00',
        'img_url': 'static/assets/shower.webp'
    },
]

kitchen_list = [
    {
        'id': 1,
        'title': 'Stove',
        'description': 'The heart of the kitchen',
        'price': '750.00',
        'img_url': 'static/assets/stove.jpeg'
    },
    {
        'id': 2,
        'title': 'Refridgerator',
        'description': 'Keep your food cold and fresh',
        'price': '900.00',
        'img_url': 'static/assets/fridge.jpeg'
    },
    {
        'id': 3,
        'title': 'Pots and Pans',
        'description': 'Somethings about to smell great!',
        'price': '220.00',
        'img_url': 'static/assets/pots.jpeg'
    },
    {
        'id': 4,
        'title': 'Dishwasher',
        'description': 'Making cleaning a breeze',
        'price': '440.00',
        'img_url': 'static/assets/dishwasher.jpeg'
    },
]

# Create your views here.


def index(request):
    response = render(request, 'generica_app/index.html')
    return response


def products(request):
    query = request.GET.get('query')
    # auth = OAuth1(os.environ['apikey'], os.environ['secretkey']) .env file not working
    auth = OAuth1('4863a4c3a62e416da5807ea7494b34c4',
                  'd5d493e9dd16400f9825f1a7baa57bb1')
    endpoint = f"http://api.thenounproject.com/icon/{query}"

    API_response = requests.get(endpoint, auth=auth)
    JSON_API_response = json.loads(API_response.content)
    image_url = JSON_API_response['icon']['preview_url']
    return JsonResponse({'url': image_url})

def kitchen(request):
    data = {'kitchen_list': kitchen_list}
    response = render(request, 'generica_app/kitchen.html', data)
    return response

def bed_and_bath(request):
    data = {'bed_and_bath_list': bed_and_bath_list}
    response = render(request, 'generica_app/bed_and_bath.html', data)
    return response

def electronics(request):
    data = {'electronics_list': electronics_list}
    response = render(request, 'generica_app/electronics.html', data)
    return response

def outdoors(request):
    data = {'outdoors_list': outdoors_list}
    response = render(request, 'generica_app/outdoors.html', data)
    return response


def cart(request):
    response = render(request, 'generica_app/cart.html')
    return response


def searchpage(request):
    response = render(request, 'generica_app/searchpage.html')
    return response
