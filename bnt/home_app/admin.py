from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Variant)




class CategoryAdmin(admin.ModelAdmin):
	list_display=('id','title')
admin.site.register(Category,CategoryAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title','category','is_featured')
    list_editable=('is_featured',)
admin.site.register(Product,ProductAdmin)


# Product Attribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('id','image_tag','product','price','variant','status')
    list_editable=('status',)
admin.site.register(ProductAttribute,ProductAttributeAdmin)