from django.shortcuts import render, HttpResponse
from products import views as product_helpers
from cart import views as cart_helpers
from django.core.paginator import Paginator
from products.models import Property

import math

# Create your views here.


def home(request, products=None):

    if not products:
        products = product_helpers.get_products(request)

    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    # ?page=2

    return render(request, 'frontend/home.html', {
        "products": products,
    })


def filter_by_category(request, category_id):
    products = product_helpers.filter_by_category(request, category_id)
    attributes = Property.objects.filter(product__in=products).order_by(
        'name').values('name', 'description')
    attributes_temp = []
    lastName = ""
    for att in attributes:
        if att['name'] == lastName:
            attributes_temp.append(att)
        else:
            lastName = att['name']
            attributes_temp.append({'globalName': att['name']})
            attributes_temp.append(att)

    return render(request, 'frontend/home.html', {"products": products, 'propertiesCust': attributes_temp})


def product_info(request, product_id):
    product = product_helpers.detail(request, product_id)
    photos = product_helpers.product_photos(request, product_id)
    properties = product_helpers.get_all_product_properties(
        request, product_id)

    thumb_rows = []

    temp = 0
    # Thumbnail row to make
    chunks = math.ceil(len(photos)/4)

    for i in range(chunks):
        t = []
        for j in range(min(4, len(photos) - temp)):
            temp += 1

            t.append(photos[i * 4 + j])
        thumb_rows.append(t)

    data = {
        "product": product,
        "photos": photos,
        "thumb_rows": thumb_rows,
        "properties": properties
    }

    return render(request, 'frontend/components/product.html', data)


def faq(request):
    return render(request, 'frontend/faq.html')


def contact(request):
    return render(request, 'frontend/contact.html')


def about(request):
    return render(request, 'frontend/about.html')


def cart(request):
    cart_info = cart_helpers.test_request(request)
    return render(request, 'frontend/components/cart/index.html')
