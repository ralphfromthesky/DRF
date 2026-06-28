from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    