from django.db import models


# Create your models here.

class AvailabilitySize(models.Model):
    """
    Model representing a specific size of a product, including its price, count, and discount.
    """
    size_type = models.CharField(max_length=255)
    price = models.FloatField()
    count = models.IntegerField()
    discount = models.FloatField()

    def __str__(self):
        return self.size_type


class VarietyImage(models.Model):
    """
    Model representing an image of a specific variety of a product.
    """
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url


class Variety(models.Model):
    """
    Model representing a specific variety of a product, including its color, available sizes, and images.
    """
    color = models.CharField(max_length=50)
    available_sizes = models.ManyToManyField(AvailabilitySize)
    images = models.ManyToManyField(VarietyImage)

    def __str__(self):
        return self.color


class Category(models.Model):
    """
    Model representing a category of products.
    """
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Brand(models.Model):
    """
    Model representing a brand of products.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model representing a product, including its name, brand, category, features, and varieties.
    """
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    features = models.JSONField()
    variety = models.ManyToManyField(Variety)

    def __str__(self):
        return self.name
