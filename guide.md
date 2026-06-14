-  python -m venv venv
- venv\Scripts\activate
- pip install django djangorestframework
- django-admin startproject config .
- python manage.py startapp api

run server - python manage.py runserver

-create a models inside models.py

class Product(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name

-python manage.py makemigrations
-python manage.py migrate

-create a serializers.py then in file inside this

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'descriptions', 'price', 'available', 'quantity']

-=--or this is the shortcuts ----

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



After the model is created and migrated, the next step is serializers.
The usual order is:

Model – define the data (you did this)
Migrate – create the table (you did this)
Serializer – define how the model is converted to/from JSON for the API
Views – API endpoints that use the serializer (list, create, get one, update, delete)
URLs – map routes (e.g. /api/products/) to those views


-add this INSTALLED_APPS = [
      'rest_framework', --> important need to add this
    'api' --> name of the created app
]

-add this in bottom of main settings.py if you don want to see web pages

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}

