from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

print('this is my new version1 change')

print('this is my new change')

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category','description']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)

print('this is my version1 by git change')

