from django.shortcuts import render, HttpResponse, redirect
from products import views as product_helpers
from cart import views as cart_helpers
from django.core.paginator import Paginator
from products.models import Property
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from frontend.validators import len_validator, password_validator, unique_validator
import math

# Create your views here.


def home(request, products=None, message=None):
    term = request.POST.get('term')

    if not products:
        products = product_helpers.get_products(request)


    if term:
        term = request.POST.get('term')
        products = product_helpers.search_products((term))


    if term and len(products) > 0:
        paginator = Paginator(products, len(products))
    else:
        paginator = Paginator(products, 9)


    page = request.GET.get('page')
    products = paginator.get_page(page)

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


def auth_redirect(request):
    if request.user.is_authenticated:
        return redirect('/')

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'GET':

        return render(request, 'frontend/signin.html')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            data = {
                "message": {
                    "type": 'error-msg',
                    "content": "Invalid Credentials.. Try again!"
                }
            }
            return  render(request, 'frontend/signin.html', data)

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'GET':
        return render(request, 'frontend/signup.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmation = request.POST.get('confirmation')


        message = len_validator(username, 4, 50)
        message = len_validator(password, 4, 50)
        message = len_validator(confirmation, 4, 50)
        message = password_validator(password, confirmation)

        if message['content'] == "":
            message = unique_validator(lambda: User.objects.filter(username=username), "Username already exists!")
            if message['content'] == "":
                user = User.objects.create_user(username=username, password=password)
                print(user)
                message['type'] = "success-msg"
                message["content"] = "Successfully created!"

        if message['content'] != "":
            data = {
                "message" : message
            }

        return render(request, 'frontend/signup.html', data)

def sign_out(request):
    logout(request)
    return redirect('home')



def filter_by_props(request):
    print("sadddddddddddddddddddddddd")
    filtered = product_helpers.filter_by(request)
    print(len(filtered))
    return home(request, products=filtered)
