from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    # path('', views.index, name='index'),
     path('<int:product_id>', views.detail, name='product-details'),
     path('product/<int:category_id>', views.filter_by_category, name='product-filter'),
     path('search', views.filter_by, name='product-fil')
    # path('', views.index, name='index'),
]