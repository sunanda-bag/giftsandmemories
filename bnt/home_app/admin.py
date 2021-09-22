from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Variant)
admin.site.register(BoxSize)




class CategoryAdmin(admin.ModelAdmin):
	list_display=('id','title')
admin.site.register(Category,CategoryAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title','category','is_featured')
    list_editable=('is_featured',)
admin.site.register(Product,ProductAdmin)


# Product Attribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('id','image_tag','product','price','variant','availability_status')
    list_editable=('availability_status',)
admin.site.register(ProductAttribute,ProductAttributeAdmin)


class BoxAdmin(admin.ModelAdmin):
    list_display=('id','title',)
    
admin.site.register(Box,BoxAdmin)


# Product Attribute
class BoxAttributeAdmin(admin.ModelAdmin):
    list_display=('id','image_tag','box','size','availability_status')
    list_editable=('availability_status',)
admin.site.register(BoxAttribute,BoxAttributeAdmin)



class CardAdmin(admin.ModelAdmin):
    list_display=('id','image_tag','title','availability_status')
    list_editable=('availability_status',)
    
admin.site.register(Card,CardAdmin)