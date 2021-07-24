from django.urls import path
from .views import login, register, edit
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', authapp.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
]
