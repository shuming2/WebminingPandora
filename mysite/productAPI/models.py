from django.db import models

# Groups
class Collection(models.Model):
    key = models.CharField(primary_key=True, max_length = 100)
    value = models.CharField(max_length=100)

class Category(models.Model):
    key = models.CharField(primary_key=True, max_length = 100)
    value = models.CharField(max_length=100)

class SubCategory(models.Model):
    key = models.CharField(primary_key=True, max_length=100)
    value = models.CharField(max_length=100)

class Metal(models.Model):
    key = models.CharField(primary_key=True, max_length=100)
    value = models.CharField(max_length=100)

class Material(models.Model):
    key = models.CharField(primary_key=True, max_length=100)
    value = models.CharField(max_length=100)

class Color(models.Model):
    key = models.CharField(primary_key=True, max_length=100)
    value = models.CharField(max_length=100)

class Stone(models.Model):
    key = models.CharField(primary_key=True, max_length=100)
    value = models.CharField(max_length=100)

class Theme(models.Model):
    key = models.CharField(primary_key=True, max_length=100)
    value = models.CharField(max_length=100)


# Products
class Product(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(primary_key=True, max_length=100)
    baseid = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    url = models.URLField()
    collection = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcollection = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    metal = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    theme = models.CharField(max_length=100, blank=True)
    stone = models.CharField(max_length=100)
    price = models.IntegerField()
    newest = models.BooleanField()
    description = models.CharField(max_length=200)
    image = models.ImageField()

