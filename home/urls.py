from django.contrib import admin
from django.urls import path
from .views import *

app_name = "home"

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
   
    path('portfolio', portfolio, name='portfolio'),
    path('price', price, name='price'),
    path('services', services, name='services'),

    path('blog', blog, name='blog'),
    path('blog-details/<slug>', blog_detail, name='blog-details'),
]
