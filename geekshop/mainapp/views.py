from random import sample

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import ProductCategory, Product


def products(request, pk=None):

    title = 'каталог'

    links_menu = ProductCategory.objects.all()

    main_menu = [
        {'href': 'index', 'name': 'домой'},
        {'href': 'products:index', 'name': 'продукты'},
        {'href': 'contacts', 'name': 'контакты'},
    ]

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'main_menu': main_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }
        return render(request, 'products_list.html', context=content)

    same_products = Product.objects.all()[2:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'main_menu': main_menu,
        'same_products': same_products,
        'basket': basket,
    }

    return render(request, 'products.html', context=content)
