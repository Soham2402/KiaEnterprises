from django.contrib import admin
from .models import Description, Product, Category,Image,SubProduct

from django.contrib import admin

class DescriptionInline(admin.StackedInline):  # or admin.StackedInline
    model = Description
    extra =  1

class ImagesInline(admin.StackedInline):  # or admin.StackedInline
    model = Image
    extra =  1
    
class SubProductAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]


# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Description)
admin.site.register(SubProduct,SubProductAdmin)
admin.site.register(Category)
