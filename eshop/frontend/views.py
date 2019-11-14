from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
  return render(request, 'frontend/home.html')

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