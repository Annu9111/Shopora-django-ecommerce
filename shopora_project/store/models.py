from django.db import models

# Category first
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Then Product
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name