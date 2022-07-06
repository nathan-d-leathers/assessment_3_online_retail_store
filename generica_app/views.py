from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import requests as HTTP_Client
from dotenv import load_dotenv
import json
import os
import pprint
# from .models


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


def homegoods(request):
    # context = {
    #     'items': Item.objects.all()
    # }
    # render reponse includes , context
    response = render(request, 'generica_app/homegoods.html')
    return response


def kitchen(request):
    response = render(request, 'generica_app/kitchen.html')
    return response


def bathroom(request):
    response = render(request, 'generica_app/bathroom.html')
    return response


def electronics(request):
    response = render(request, 'generica_app/electronics.html')
    return response


def outdoors(request):
    response = render(request, 'generica_app/outdoors.html')
    return response


def cart(request):
    response = render(request, 'generica_app/cart.html')
    return response


def searchpage(request):
    response = render(request, 'generica_app/searchpage.html')
    return response
