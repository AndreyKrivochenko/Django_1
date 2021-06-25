from django.shortcuts import render

title = 'каталог'
links_menu = [
        {'name': 'все'},
        {'name': 'дом'},
        {'name': 'офис'},
        {'name': 'модерн'},
        {'name': 'классика'},
]

content = {
    'title': title,
    'links_menu': links_menu,
}


def products(request):
    return render(request, 'products.html', context=content)
