from django.views import View
from django.shortcuts import render,redirect
from store.models.category import Category
from store.models.product import Product

def index(request):
    prods = None
    catergory = Category.get_all_categories()
    categoryID=request.GET.get('category')
    if categoryID:
        prods = Product.get_all_products_by_categoryid(categoryID)
    else:
        prods = Product.get_all_products()
    data={}
    data['product'] = prods
    data['categories'] = catergory
    print(request.session.get('customer_email'))
    return render(request,'index.html',data)
