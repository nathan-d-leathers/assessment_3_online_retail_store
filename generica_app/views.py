from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from requests_oauthlib import OAuth1
import requests as HTTP_Client
import requests
import json
from dotenv import load_dotenv
import os
import pprint
load_dotenv()

product_list = [
    [
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
    ],
    [
        {
            'id': 5,
            'title': 'Tent',
            'description': 'Spend a night sleeping under the stars',
            'price': '300.00',
            'img_url': 'static/assets/tent.jpeg'
        },
        {
            'id': 6,
            'title': 'Grill',
            'description': 'Charcoal not included',
            'price': '450.00',
            'img_url': 'static/assets/grill.webp'
        },
        {
            'id': 7,
            'title': 'Canoe',
            'description': 'Check out a new kind of Streaming',
            'price': '750.00',
            'img_url': 'static/assets/canoe.jpeg'
        },
        {
            'id': 8,
            'title': 'Bicycle',
            'description': 'Eco-friendly Transportation powered by YOU',
            'price': '1200.00',
            'img_url': 'static/assets/bicycle.jpeg'
        },
    ],
    [
        {
            'id': 9,
            'title': 'Bed',
            'description': 'Spend a third of your life in comfort',
            'price': '2400.00',
            'img_url': 'static/assets/bed.jpeg'
        },
        {
            'id': 10,
            'title': 'Toilet',
            'description': 'A porcelain throne fit for a king',
            'price': '150.00',
            'img_url': 'static/assets/toilet.jpeg'
        },
        {
            'id': 11,
            'title': 'Dresser',
            'description': 'Wardrobe storage at an affordable price',
            'price': '280.00',
            'img_url': 'static/assets/dresser.jpeg'
        },
        {
            'id': 12,
            'title': 'Shower',
            'description': 'Wake up feeling refreshed',
            'price': '120.00',
            'img_url': 'static/assets/shower.webp'
        },
    ],
    [
        {
            'id': 13,
            'title': 'Stove',
            'description': 'The heart of the kitchen',
            'price': '750.00',
            'img_url': 'static/assets/stove.jpeg'
        },
        {
            'id': 14,
            'title': 'Refrigerator',
            'description': 'Keep your food cold and fresh',
            'price': '900.00',
            'img_url': 'static/assets/fridge.jpeg'
        },
        {
            'id': 15,
            'title': 'Pots and Pans',
            'description': 'Somethings about to smell great!',
            'price': '220.00',
            'img_url': 'static/assets/pots.jpeg'
        },
        {
            'id': 16,
            'title': 'Dishwasher',
            'description': 'Making cleaning a breeze',
            'price': '440.00',
            'img_url': 'static/assets/dishwasher.jpeg'
        },
    ]
]

# Create your views here.

# Demo that cart will populate from this list
# Issue I am trying to solve:How do I retrieve data from category lists when button is submitted and append that data into this list

cart_list = [
    '1',
    '2',
    '3',
]


def index(request):
    response = render(request, 'generica_app/index.html')
    return response


def products(request):
    query = request.GET.get('query')
    auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])

    # Oauth1 not working, says module not found
    # had to install pip instal requests requests_oauthlib to use

    endpoint = f"http://api.thenounproject.com/icon/{query}"

    API_response = requests.get(endpoint, auth=auth)
    JSON_API_response = json.loads(API_response.content)
    image_url = JSON_API_response['icon']['preview_url']
    return JsonResponse({'url': image_url})


def kitchen(request):
    kitchen_list = product_list[3]
    data = {'kitchen_list': kitchen_list}
    response = render(request, 'generica_app/kitchen.html', data)
    return response


def bed_and_bath(request):
    bed_and_bath_list = product_list[2]
    data = {'bed_and_bath_list': bed_and_bath_list}
    response = render(request, 'generica_app/bed_and_bath.html', data)
    return response


def electronics(request):
    electronics_list = product_list[0]
    data = {'electronics_list': electronics_list}
    response = render(request, 'generica_app/electronics.html', data)
    return response


def outdoors(request):
    outdoors_list = product_list[1]
    data = {'outdoors_list': outdoors_list}
    response = render(request, 'generica_app/outdoors.html', data)
    return response


def cart(request):
    data = {"cart_list": cart_list}
    response = render(request, 'generica_app/cart.html', data)
    return response


def searchpage(request):
    response = render(request, 'generica_app/searchpage.html')
    return response


# not working cart function

# def add_to_cart(request):
#     new_cart_item = {
#             img_url: "img_url",
#             title: "title",
#             price: "price",
#         }
#     cart_list.append(new_cart_item)
