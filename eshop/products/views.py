from decimal import *

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, QueryDict
from products.models import Product, Category, Property, ProductImage


# Create your views here.


def get_products(request):
    products = Product.objects.all()
    return products


def get_categories(request):
    return Category.objects.all()


def get_product_categories(request):
    pass


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return product


def product_photos(request, product_id):
    photos = ProductImage.objects.filter(product_id=product_id)
    return photos


def get_all_product_properties(request, product_id):
    properties = Property.objects.filter(product_id=product_id)
    return properties


def filter_by_category(request, category_id):
    categories = Category.objects.get(
        pk=category_id).get_descendants(include_self=True)

    product_list = Product.objects.filter(categories__in=categories)

    return product_list


def filter_by(request):
    try:
        minPrice = Decimal(request.GET['minPrice'])
    except:
        minPrice = 0
        print("Cannot convert")

    try:
        maxPrice = Decimal(request.GET['maxPrice'])
        if minPrice > maxPrice or minPrice < 0 or maxPrice < 0:
            raise Exception('Bad price')
    except:
        maxPrice = 10000000
        print("Cannot convert")

    values_s = dict(request.GET)
    l = []
    [l.extend(v) for k, v in values_s.items()]
    attributes = Property.objects.filter(
        name__in=values_s.keys(), description__in=l)
    product_list = Product.objects.filter(
        property__in=attributes, price__gte=minPrice, price__lte=maxPrice).distinct()

    return render(request, 'products/allproducts.html', {
        'products': product_list,
    })

def search_products(query):
    return Product.objects.filter(title__icontains=query)

