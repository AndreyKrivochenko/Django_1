from django.shortcuts import render

title = 'каталог'
links_menu = [
        {'name': 'все'},
        {'name': 'дом'},
        {'name': 'офис'},
        {'name': 'модерн'},
        {'name': 'классика'},
]

main_menu = [
    {'href': 'index', 'name': 'домой'},
    {'href': 'products:index', 'name': 'продукты'},
    {'href': 'contacts', 'name': 'контакты'},
]

content = {
    'title': title,
    'links_menu': links_menu,
    'main_menu': main_menu,
}


def products(request):
    return render(request, 'products.html', context=content)
