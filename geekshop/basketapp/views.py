from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def basket(request):
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user).order_by('product__category')
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


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))

    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        _basket = Basket.objects.filter(user=request.user).order_by('product__category')

        context = {
            'basket': _basket,
        }

        result = render_to_string('basketapp/inсludes/inc_basket_list.html', context=context)

        return JsonResponse({'result': result})
