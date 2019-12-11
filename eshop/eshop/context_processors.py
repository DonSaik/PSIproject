from products.models import Category, Property


def categories_list(request):
    # https://stackoverflow.com/questions/28419062/find-second-level-children-in-django-mptt
    # Category https://django-mptt.readthedocs.io/en/latest/technical_details.html
    categories_list = Category.objects.filter(level__lte=1)
    return {'categories': categories_list}


def properties_list(request):
    attributes = Property.objects.order_by(
        'name').values('name', 'description').distinct()
    attributes_temp = []
    lastName = ""
    for att in attributes:
        if att['name'] == lastName:
            attributes_temp.append(att)
        else:
            lastName = att['name']
            attributes_temp.append({'globalName': att['name']})
            attributes_temp.append(att)

    return {'properties': attributes_temp}
