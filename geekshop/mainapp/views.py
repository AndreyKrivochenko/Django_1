from random import sample

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return sample(list(products), 1)[0]


def get_same_product(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)
    return same_products


def products(request, pk=None, page=1):

    title = 'каталог'

    links_menu = ProductCategory.objects.all()

    main_menu = [
        {'href': 'index', 'name': 'домой'},
        {'href': 'products:index', 'name': 'продукты'},
        {'href': 'contacts', 'name': 'контакты'},
    ]

    basket = get_basket(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.filter(is_deleted=False).order_by('price')
            category = {'pk': 0, 'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(is_deleted=False, category__pk=pk).order_by('price')

        paginator = Paginator(products, 2)

        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_menu': links_menu,
            'main_menu': main_menu,
            'category': category,
            'products': products_paginator,
            'basket': basket,
        }
        return render(request, 'products_list.html', context=content)

    hot_product = get_hot_product()
    same_products = get_same_product(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'main_menu': main_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
    }

    return render(request, 'products.html', context=content)


def product(request, pk):
    title = 'продукты'

    context = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'product.html', context)
