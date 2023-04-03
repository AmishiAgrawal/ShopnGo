from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('home/',views.index),
    path('contact/',views.contact),
    path('about/',views.about),
    path('cart/',views.cart),
    path('wishlist/',views.wishlist),
    path('categories/<str:my_category>',views.categories),
    path('tracker/',views.tracker),
    path('checkout/',views.checkout),
    path('productview/<int:p_id>/',views.productview),
    path('search/',views.search),
]
