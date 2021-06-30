from random import sample

from django.shortcuts import render

from .models import ProductCategory, Product

title = 'каталог'

links_menu = [
    {'name': 'все'}
]

links_menu += ProductCategory.objects.all()

main_menu = [
    {'href': 'index', 'name': 'домой'},
    {'href': 'products:index', 'name': 'продукты'},
    {'href': 'contacts', 'name': 'контакты'},
]

content = {
    'title': title,
    'links_menu': links_menu,
    'main_menu': main_menu,
    'products': sample(list(Product.objects.all()), 3),
}


def products(request):
    return render(request, 'products.html', context=content)
