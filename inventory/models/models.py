from django.db import models

class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=100)
    quantity = models.BigIntegerField(default=0)
    
    def __str__(self):
        return self.item_name