from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('home',views.index),
    path('contact',views.contact),
    path('about',views.about),
    path('cart',views.cart),
    path('wishlist',views.wishlist),
    path('categories',views.categories),
    path('tracker',views.tracker),
    path('checkout',views.checkout),
    path('productview',views.productview),
    path('search',views.search),
]
