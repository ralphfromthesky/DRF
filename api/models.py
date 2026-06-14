from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name