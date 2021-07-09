from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        main_menu = [
            {'href': 'index', 'name': 'домой'},
            {'href': 'products:index', 'name': 'продукты'},
            {'href': 'contacts', 'name': 'контакты'},
        ]
        context = {
            'basket': basket,
            'main_menu': main_menu,
        }
        return render(request, 'basketapp/basket.html', context)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    content = {}
    return render(request, 'basketapp/basket.html', content)