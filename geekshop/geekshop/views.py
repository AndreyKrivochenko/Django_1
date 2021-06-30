from random import sample

from django.shortcuts import render
from mainapp.models import Product


links_menu = [
    {'href': 'index', 'name': 'домой'},
    {'href': 'products:index', 'name': 'продукты'},
    {'href': 'contacts', 'name': 'контакты'},
]

title_index = 'магазин'
title_contacts = 'контакты'

content_index = {
    'main_menu': links_menu,
    'title': title_index,
    'products': sample(list(Product.objects.all()), 4),
}

content_contacts = {
    'main_menu': links_menu,
    'title': title_contacts,
}


def index(request):
    return render(request, 'index.html', context=content_index)


def contacts(request):
    return render(request, 'contact.html', context=content_contacts)
