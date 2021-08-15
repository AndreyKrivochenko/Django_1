from django.urls import path
from django.views.decorators.cache import cache_page

from .views import products, product, products_ajax

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:pk>/', products, name='category'),
    path('category/<int:pk>/ajax/', cache_page(3600)(products_ajax)),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
    path('category/<int:pk>/page/<int:page>/ajax/', cache_page(3600)(products_ajax)),
    path('product/<int:pk>/', product, name='product'),
]
