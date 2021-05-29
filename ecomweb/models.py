from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    product_description = models.TextField()
    image = models.ImageField(upload_to="product_images")

    def __str__(self):
        return self.title
