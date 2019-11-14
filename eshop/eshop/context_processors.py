from products.models import Category

def categories_list(request):
    #https://stackoverflow.com/questions/28419062/find-second-level-children-in-django-mptt
    #Category https://django-mptt.readthedocs.io/en/latest/technical_details.html
    categories_list = Category.objects.filter(level__lte=1)
    for v in categories_list:
        print(v)
    return {'categories': categories_list}


