from django.db import models
from django.shortcuts import reverse

from django.utils.html import mark_safe
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='1. Categories'
        


# class Label(models.Model):
#     title = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name_plural='2. Labels'


# Variant


class Variant(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='2. Variants'

    def __str__(self):
        return self.title


# Variant
class BoxSize(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='3. Box Sizes'

    def __str__(self):
        return self.title


# Box Model
class Box(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()

    class Meta:
        verbose_name_plural='4. Boxes'

    def __str__(self):
        return self.title


# Box Attribute
class BoxAttribute(models.Model):
    box=models.ForeignKey(Box,on_delete=models.CASCADE)
    size=models.ForeignKey(BoxSize,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    availability_status=models.BooleanField(default=True)
   
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name_plural='5. BoxAttributes'

    def __str__(self):
        return self.box.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))



# Cards Model
class Card(models.Model):
    title=models.CharField(max_length=200)
    availability_status=models.BooleanField(default=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
   
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    class Meta:
        verbose_name_plural='6. Cards'

    def __str__(self):
        return self.title


# Product Model
class Product(models.Model):
    title=models.CharField(max_length=200)
    
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    # brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    
    is_featured=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='7. Products'

    def __str__(self):
        return self.title

# Product Attribute
class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    variant=models.ForeignKey(Variant,on_delete=models.CASCADE)
    availability_status=models.BooleanField(default=True)
    price=models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
   
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name_plural='8. ProductAttributes'

    def __str__(self):
        return self.product.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))





# # Order
# status_choice=(
#         ('process','In Process'),
#         ('shipped','Shipped'),
#         ('delivered','Delivered'),
#     )

# class CartOrder(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     total_amt=models.FloatField()
#     paid_status=models.BooleanField(default=False)
#     order_dt=models.DateTimeField(auto_now_add=True)
#     order_status=models.CharField(choices=status_choice,default='process',max_length=150)

#     class Meta:
#         verbose_name_plural='4. Orders'



# # OrderItems
# class CartOrderItems(models.Model):
#     order=models.ForeignKey(CartOrder,on_delete=models.CASCADE)
#     invoice_no=models.CharField(max_length=150)
#     item=models.CharField(max_length=150)
#     image=models.CharField(max_length=200)
#     qty=models.IntegerField()
#     price=models.FloatField()
#     total=models.FloatField()

#     class Meta:
#         verbose_name_plural='5. Order Items'

#     def image_tag(self):
#         return mark_safe('<img src="/images/%s" width="50" height="50" />' % (self.image))



# # Product Review
# RATING=(
#     (1,'1'),
#     (2,'2'),
#     (3,'3'),
#     (4,'4'),
#     (5,'5'),
# )
# class ProductReview(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
#     review_text=models.TextField()
#     review_rating=models.CharField(choices=RATING,max_length=150)

#     class Meta:
#         verbose_name_plural='6. Reviews'

#     def get_review_rating(self):
#         return self.review_rating



# # WishList
# class Wishlist(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)

#     class Meta:
#         verbose_name_plural='7. Wishlist'



# # AddressBook
# class UserAddressBook(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     mobile=models.CharField(max_length=50,null=True)
#     address=models.TextField()
#     status=models.BooleanField(default=False)

#     class Meta:
#         verbose_name_plural='8. AddressBook'
