from django.shortcuts import render, HttpResponse
from products import views as product_helpers


# Create your views here.

def home(request, products=None):

  if not products:
    products = product_helpers.get_products(request)
    categories = product_helpers.get_categories(request)


  return render(request, 'frontend/home.html', {
    "products": products,
    "categories": categories
    })



def filter_by_category(request, category_id):
  products = product_helpers.filter_by_category(request,category_id)
  return render(request, 'frontend/home.html', {"products": products})


def product_info(request, product_id):
  data = {

  }
  return render(request, 'frontend/product.html', data)

def faq(request):
  return render(request, 'frontend/faq.html')

def contact(request):
  return render(request, 'frontend/contact.html')

def about(request):
  return render(request, 'frontend/about.html')