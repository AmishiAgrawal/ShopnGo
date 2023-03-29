from django.shortcuts import render
from math import ceil
from . models import *


def index(request):
    products = Products.objects.all()
    # categories = Products.objects.all().values('product_category')
    # print(categories)
    # print(type(categories))
    print(products.values('product_img'))
    # products = products.values('product_img')
    print(products)
    print(len(products))
    
    range2 = len(products) % 4
    range2 = 4 - range2
    print(range2)
    allProducts = []
    prod_categories = Products.objects.values('product_category','product_id')
    categories = { item['product_category'] for item in prod_categories}
    print('---------------')
    print(categories)
    for category in categories:
        n = len(products)
        number_of_slides = n//4 + ceil((n/4) - (n//4))
        p_category = [category]
        products = Products.objects.filter(product_category=category)
        range2 = len(products) % 4
        range2 = 4 - range2
        range2 = range(range2)
        print(range2)
        allProducts.append([products,range(1,number_of_slides),number_of_slides,range2,p_category])
        print('************',allProducts,"*************")

    # return render(request,'MyShop/index.html',{'slides':number_of_slides,'range':range(number_of_slides),'range2':range(range2), 'product':products,'categories':categories})
    return render(request,'MyShop/index.html',{'allProducts':allProducts})

def about(request):
    return render(request,'MyShop/about.html')

def contact(request):
    return render(request,'MyShop/contact.html')

def wishlist(request):
    return render(request,'MyShop/wishlist.html')

def cart(request):
    return render(request,'MyShop/cart.html')

def categories(request):
    return render(request,'MyShop/categories.html')

def checkout(request):
    return render(request,'MyShop/checkout.html')

def productview(request):
    return render(request,'MyShop/productview.html')

def tracker(request):
    return render(request,'MyShop/tracker.html')

def search(request):
    return render(request,'MyShop/search.html')
