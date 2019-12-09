from django.shortcuts import render, HttpResponse
from products import views as product_helpers
from django.core.paginator import Paginator
from products.models import Property
# Create your views here.

def home(request, products=None):

  if not products:
    products = product_helpers.get_products(request)


  paginator = Paginator(products, 9)
  page = request.GET.get('page')
  products = paginator.get_page(page)

  #?page=2


  return render(request, 'frontend/home.html', {
    "products": products,
    })



def filter_by_category(request, category_id):
  products = product_helpers.filter_by_category(request,category_id)
  attributes = Property.objects.filter(product__in=products).order_by('name').values('name', 'description')
  attributes_temp = []
  lastName = ""
  for att in attributes:
    print(att['name'])
    if att['name'] == lastName:
      attributes_temp.append(att)
    else:
      lastName = att['name']
      attributes_temp.append({'globalName': att['name']})
      attributes_temp.append(att)

  return render(request, 'frontend/home.html', {"products": products, 'propertiesCust': attributes_temp})


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