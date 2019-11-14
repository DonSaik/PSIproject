from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from products.models import Product, Category


# Create your views here.


def get_products(request):
    products  = Product.objects.all()
    return products

def get_categories(request):
    return Category.objects.all()
    
def get_product_categories(request):
    pass


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/product.html', {'product': product})


def filter_by_category(request, category_id):
    categories = Category.objects.get(pk=category_id).get_descendants(include_self=True)
    for c in categories:
        print(c)
    list = Product.objects.filter(categories__in=categories)
    for c in list:
        print(c)
    
    return list;