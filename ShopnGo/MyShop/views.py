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
    # print('---------------')
    # print(categories)
    for category in categories:
        n = len(products)
        number_of_slides = n//4 + ceil((n/4) - (n//4))
        p_category = [category]
        products = Products.objects.filter(product_category=category)
        range2 = len(products) % 4
        range2 = 4 - range2
        range2 = range(range2-1)
        # print(range2)
        allProducts.append([products,range(1,number_of_slides),number_of_slides,range2,p_category])
        # print('************',allProducts,"*************")

    # return render(request,'MyShop/index.html',{'slides':number_of_slides,'range':range(number_of_slides),'range2':range(range2), 'product':products,'categories':categories})
    return render(request,'MyShop/index.html',{'allProducts':allProducts})

def about(request):
    return render(request,'MyShop/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        issue = request.POST.get('issue')

        msg = Contact(user_name=name,email=email,phone=phone,issue=issue)
        msg.save()
    return render(request,'MyShop/contact.html')

def wishlist(request):
    return render(request,'MyShop/wishlist.html')

def cart(request):
    return render(request,'MyShop/cart.html')

def categories(request,my_category):
    product = Products.objects.filter(product_category=my_category)
    return render(request,'MyShop/categories.html',{'products':product}) 

def checkout(request):
    return render(request,'MyShop/checkout.html')

def productview(request,p_id):
    product = Products.objects.get(product_id = p_id)
    product_ldesc = str(product.product_ldesc).replace(';','.')
    product_ldesc = product_ldesc.split('. ')
    product_ldesc = [ line + '.' for line in product_ldesc ]
    print(product_ldesc)
    return render(request,'MyShop/productview.html',{'product':product,'ldesc':product_ldesc})

def tracker(request):
    return render(request,'MyShop/tracker.html')

def search(request):
    return render(request,'MyShop/search.html')
