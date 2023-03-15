from django.shortcuts import render

def index(request):
    return render(request,'MyShop/index.html')

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
