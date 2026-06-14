from django.db import models

class datas(models.Model):
    descriptions = models.CharField(max_length=200)
    data = models.TextField()
    is_active = models.BooleanField()
    
    def __str__(self):
        return self.descriptions