from random import sample

from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product


links_menu = [
    {'href': 'index', 'name': 'домой'},
    {'href': 'products:index', 'name': 'продукты'},
    {'href': 'contacts', 'name': 'контакты'},
]

title_index = 'магазин'
title_contacts = 'контакты'


def index(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    content_index = {
        'main_menu': links_menu,
        'title': title_index,
        'products': sample(list(Product.objects.all()), 4),
        'basket': basket,
    }
    return render(request, 'index.html', context=content_index)


def contacts(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    content_contacts = {
        'main_menu': links_menu,
        'title': title_contacts,
        'basket': basket,
    }
    return render(request, 'contact.html', context=content_contacts)
