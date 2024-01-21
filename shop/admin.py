from django.contrib import admin
from .models import Products 
# Register your models here.
from .models import Order

admin.site.site_header = "E-Commerce Admin"
admin.site.site_title = "ABC shopping"
admin.site.index_title = "Manage ABC shopping"


class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = 'Default Category'
    list_display = ('title', 'price', 'discounted_price', 'category', 'description',)
    search_fields = ('title', 'category',)
    actions = ('change_category_to_default', )
    fields = ('title', 'price', 'discounted_price',)
    list_editable = ('price', 'discounted_price',)

admin.site.register(Products, ProductAdmin)
admin.site.register(Order)
