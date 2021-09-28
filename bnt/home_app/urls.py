from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('products/', views.products, name='products'),
    path('premade/', views.premade, name='premade'),
    path('build-a-box/', views.build_a_box, name='build_a_box'),
    # path('products/<str:id>/', views.product_detail, name= 'product-detail'),
    
    # path('products-filter/',views.products_filter,name="products_filter"),
    # path('category-product-list/<int:cat_id>/',views.category_product_list,name='category-product-list'),

    path('add-to-cart/',views.add_to_cart,name='add_to_cart'),
    # path('cart/',views.cart_list,name='cart'),
    # path('delete-from-cart/',views.delete_cart_item,name='delete-from-cart'),
    # path('update-cart/',views.update_cart_item,name='update-cart'),

    path('accounts/signup/',views.signup,name='signup'),
    # path('checkout/',views.checkout,name='checkout'),
    # path('paypal/', include('paypal.standard.ipn.urls')),
    # path('payment-done/', views.payment_done, name='payment_done'),
    # path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),

    # # User Section Start
    # path('my-dashboard/',views.my_dashboard, name='my_dashboard'),
    # path('my-orders/',views.my_orders, name='my_orders'),
    # path('my-orders-items/<int:id>/',views.my_order_items, name='my_order_items'),
    # # End

    # # Wishlist
    # path('add-wishlist/',views.add_wishlist, name='add_wishlist'),
    # path('my-wishlist/',views.my_wishlist, name='my_wishlist'),

    # # My Reviews
    # path('my-reviews/',views.my_reviews, name='my-reviews'),
    # path('save-review/<int:pid>/',views.save_review, name='save-review'),

    # # My AddressBook
    # path('my-addressbook/',views.my_addressbook, name='my-addressbook'),
    # path('add-address/',views.save_address, name='add-address'),
    # path('activate-address/',views.activate_address, name='activate-address'),
    # path('update-address/<int:id>/',views.update_address, name='update-address'),

    # path('edit-profile/',views.edit_profile, name='edit-profile'),

    # path('terms/', views.terms, name='terms'),
    
    
]
