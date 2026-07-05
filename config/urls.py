"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('user/', include('users.urls')),
    path('profiles/', include('profiles.urls')),
    path('settings/' , include('settings.urls')),
    path('products/', include('products.urls')),
    path('products_api/', include('products.products.api_urls')),
    path('data/', include('data.urls.urls')),
    path('data_api/', include('data.urls.api_urls')),
    path('new_employee/', include('employee.urls.urls')),
    path('inventory', include('inventory.urls.urls'))
]
