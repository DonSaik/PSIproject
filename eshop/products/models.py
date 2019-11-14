from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.


class Category (MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        parent = ""
        if(self.parent is not None):
             parent = self.parent

        return '%s / %s' % (parent, self.name)



class Measurement(models.Model):
    unit = models.CharField(max_length=50, blank=True)
    value = models.FloatField()

    def __str__(self):
        return '%s %s' % (self.value, self.unit)


class Property(models.Model):
    name = models.CharField(max_length=60)
    measurement = models.ForeignKey(Measurement, null=True, blank=True, on_delete= models.SET_NULL)
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    productCode = models.CharField(max_length=30, default="")
    categories = models.ForeignKey(Category, default=1, blank=True, on_delete=models.CASCADE)
    properties = models.ManyToManyField(Property)

    def __str__(self):
        return self.title


def upload_path_handler(instance, filename):
    return "product_{id}/{file}".format(id=instance.product.id, file=filename)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=  upload_path_handler)

    def __str__(self):
        return self.image.url


