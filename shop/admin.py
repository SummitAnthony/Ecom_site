from django.contrib import admin
from .models import Products 
# Register your models here.
from .models import Order
admin.site.register(Products)
admin.site.register(Order)
