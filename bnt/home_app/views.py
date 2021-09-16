from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import *
# from django.core.mail import send_mail

# from django.http.response import JsonResponse
# from django.template.loader import render_to_string
# from django.core.mail import send_mail

# from django.db.models import Max, Min, Count, Avg
# from django.db.models.functions import ExtractMonth

from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# # paypal
# from django.urls import reverse
# from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt
# from paypal.standard.forms import PayPalPaymentsForm


def home(request):

    # products = Product.objects.all()
    # featured_prod = Product.objects.filter(is_featured=True).order_by('-id')
    # new_prod = Product.objects.filter(is_new=True).order_by('-id')
    # categories = Category.objects.all()

    # context = {'featured_prod': featured_prod, 'products': products,
    #            'new_prod': new_prod, 'categories': categories}
    context={}
    return render(request, 'home_app/index.html', context)


# # Search
# def search(request):

#     q = request.GET['q']
#     data = Product.objects.filter(title__icontains=q).order_by('-id')
#     return render(request, 'search.html', {'data': data})


def about(request):

#     categories = Category.objects.all()
#     context = {'categories': categories}
    context = {}
    return render(request, 'home_app/about.html', context)


def products(request):

    categories = Category.objects.all()
    labels = Variant.objects.all()
    products = Product.objects.all()
#     minMaxPrice = Product.objects.aggregate(
#         Min('discount_price'), Max('discount_price'))
#     # products = myFilter.qs

    data = {'products': products,
#             'labels': labels,
            'categories': categories,
#             'minMaxPrice': minMaxPrice,
            }
    # data = {}
    return render(request, 'home_app/product.html', data)


# # Filter data
# def products_filter(request):

#     categories = request.GET.getlist('category[]')
#     # brands=request.GET.getlist('brand[]')
#     # sizes=request.GET.getlist('size[]')
#     minprice = (int(float(request.GET['minPrice'])))
#     maxprice = (int(float(request.GET['maxPrice'])))

#     allProducts = Product.objects.all().order_by('-id').distinct()
#     allProducts = allProducts.filter(discount_price__gte=minprice)
#     allProducts = allProducts.filter(discount_price__lte=maxprice)

#     if len(categories) > 0:
#         allProducts = allProducts.filter(
#             category__id__in=categories).distinct()

#     t = render_to_string('products_filter.html', {'data': allProducts})
#     return JsonResponse({'data': t})


# def product_detail(request, id):

#     categories = Category.objects.all()
#     product = Product.objects.get(id=id)
#     products_all = Product.objects.all()
#     related_products = Product.objects.filter(
#         category=product.category).exclude(id=id)[:4]
#     # Check
#     canAdd = True
#     reviewCheck = ProductReview.objects.filter(
#         user=request.user, product=product).count()
#     if request.user.is_authenticated:
#         if reviewCheck > 0:
#             canAdd = False
#     # End

#     # Fetch reviews
#     reviews = ProductReview.objects.filter(product=product)
#     # End

#     # Fetch avg rating for reviews
#     avg_reviews = ProductReview.objects.filter(
#         product=product).aggregate(avg_rating=Avg('review_rating'))
#     # End

#     context={'product': product, 'products_all': products_all,
#                'categories': categories, 'related_products': related_products,'canAdd': canAdd, 'reviews': reviews, 'avg_reviews': avg_reviews}
#     return render(request, 'product_detail.html', context)


# # Products according to the category
# def category_product_list(request, cat_id):

#     categories = Category.objects.all()
#     category_with_id = Category.objects.get(id=cat_id)
#     cat_prods = Product.objects.filter(
#         category=category_with_id).order_by('-id')
#     minMaxPrice = Product.objects.aggregate(
#         Min('discount_price'), Max('discount_price'))

#     return render(request, 'category_product_list.html', {
#         'categories': categories,
#         'cat_prods': cat_prods,
#         'category_with_id': category_with_id,
#         'minMaxPrice': minMaxPrice,
#     })


# # Add to cart
# def add_to_cart(request):
#     # del request.session['cartdata']
#     cart_p = {}
#     cart_p[str(request.GET['id'])] = {
#         'image': request.GET['image'],
#         'title': request.GET['title'],
#         'qty': request.GET['qty'],
#         'discountprice': request.GET['discountprice'],
#         'actualprice': request.GET['actualprice'],
#     }
#     if 'cartdata' in request.session:
#         if str(request.GET['id']) in request.session['cartdata']:
#             cart_data = request.session['cartdata']
#             cart_data[str(request.GET['id'])]['qty'] = int(cart_p[str(
#                 request.GET['id'])]['qty'])+int(cart_data[str(request.GET['id'])]['qty'])
#             cart_data.update(cart_data)
#             request.session['cartdata'] = cart_data
#         else:
#             cart_data = request.session['cartdata']
#             cart_data.update(cart_p)
#             request.session['cartdata'] = cart_data
#     else:
#         request.session['cartdata'] = cart_p
#     return JsonResponse({'data': request.session['cartdata'], 'totalitems': len(request.session['cartdata'])})


# # Cart List Page
# def cart_list(request):

#     categories = Category.objects.all()
#     total_amt = 0
#     if 'cartdata' in request.session:
#         for p_id, item in request.session['cartdata'].items():
#             total_amt += int(item['qty'])*float(item['discountprice'])

#         return render(request, 'cart.html', {'cart_data': request.session['cartdata'],
#                                              'totalitems': len(request.session['cartdata']),
#                                              'total_amt': total_amt,
#                                              'categories': categories,
#                                              })
#     else:
#         return render(request, 'cart.html', {'cart_data': '',
#                                              'totalitems': 0,
#                                              'total_amt': total_amt,
#                                              'categories': categories
#                                              })


# # Delete Cart Item
# def delete_cart_item(request):
#     p_id = str(request.GET['id'])
#     if 'cartdata' in request.session:
#         if p_id in request.session['cartdata']:
#             cart_data = request.session['cartdata']
#             del request.session['cartdata'][p_id]
#             request.session['cartdata'] = cart_data
#     total_amt = 0
#     for p_id, item in request.session['cartdata'].items():
#         total_amt += int(item['qty'])*float(item['discountprice'])
#     t = render_to_string('cart-list.html', {'cart_data': request.session['cartdata'],
#                                             'totalitems': len(request.session['cartdata']),
#                                             'total_amt': total_amt
#                                             })
#     return JsonResponse({'data': t, 'totalitems': len(request.session['cartdata'])})


# # Update Cart Item
# def update_cart_item(request):
#     p_id = str(request.GET['id'])
#     p_qty = request.GET['qty']
#     if 'cartdata' in request.session:
#         if p_id in request.session['cartdata']:
#             cart_data = request.session['cartdata']
#             cart_data[str(request.GET['id'])]['qty'] = p_qty
#             request.session['cartdata'] = cart_data
#     total_amt = 0
#     for p_id, item in request.session['cartdata'].items():
#         total_amt += int(item['qty'])*float(item['discountprice'])
#     t = render_to_string('cart-list.html', {'cart_data': request.session['cartdata'],
#                                             'totalitems': len(request.session['cartdata']),
#                                             'total_amt': total_amt
#                                             })
#     return JsonResponse({'data': t, 'totalitems': len(request.session['cartdata'])})



# Signup Form
def signup(request):
    form = SignupForm   
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=pwd)
            login(request, user)
            return redirect('home')
    # form = SignupForm
    return render(request, 'registration/signup.html', {'form': form})


# # Checkout
# @login_required
# def checkout(request):
#     total_amt = 0
#     totalAmt = 0
#     if 'cartdata' in request.session:
#         print('///////////////////////////////////')
#         print(request.session['cartdata'])
#         for p_id, item in request.session['cartdata'].items():
#             print(item)
#             totalAmt += int(item['qty'])*float(item['discountprice'])
#             print(totalAmt)

#         # Order
#         order = CartOrder.objects.create(
#             user=request.user,
#             total_amt=totalAmt
#         )
#         # End

#         for p_id, item in request.session['cartdata'].items():
#             total_amt += int(item['qty'])*float(item['discountprice'])

#             # OrderItems
#             items = CartOrderItems.objects.create(
#                 order=order,
#                 invoice_no='INV-'+str(order.id),
#                 item=item['title'],
#                 image=item['image'],
#                 qty=item['qty'],
#                 price=item['discountprice'],
#                 total=float(item['qty'])*float(item['discountprice'])
#             )
#             # End

#         # Process Payment
#         host = request.get_host()
#         paypal_dict = {
#             'business': settings.PAYPAL_RECEIVER_EMAIL,
#             'amount': total_amt,
#             'item_name': 'OrderNo-'+str(order.id),
#             'invoice': 'INV-'+str(order.id),
#             'currency_code': 'USD',
#             'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
#             'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
#             'cancel_return': 'http://{}{}'.format(host, reverse('payment_cancelled')),
#         }
#         form = PayPalPaymentsForm(initial=paypal_dict)
#         address = UserAddressBook.objects.filter(
#             user=request.user, status=True).first()

#         return render(request, 'checkout.html', {
#                                                 'cart_data': request.session['cartdata'], 
#                                                 'totalitems': len(request.session['cartdata']), 
#                                                 'total_amt': total_amt, 
#                                                 'form': form, 
#                                                 'address': address,
#                                                   })



# # Save Review
# def save_review(request,pid):
# 	product=Product.objects.get(pk=pid)
# 	user=request.user
# 	review=ProductReview.objects.create(
# 		user=user,
# 		product=product,
# 		review_text=request.POST['review_text'],
# 		review_rating=request.POST['review_rating'],
# 		)
# 	data={
# 		'user':user.username,
# 		'review_text':request.POST['review_text'],
# 		'review_rating':request.POST['review_rating']
# 	}

# 	# Fetch avg rating for reviews
# 	avg_reviews=ProductReview.objects.filter(product=product).aggregate(avg_rating=Avg('review_rating'))
# 	# End

# 	return JsonResponse({'bool':True,
#                          'data':data,
#                          'avg_reviews':avg_reviews
#                          })



# # User Dashboard
# import calendar
# def my_dashboard(request):
# 	orders=CartOrder.objects.annotate(month=ExtractMonth('order_dt')).values('month').annotate(count=Count('id')).values('month','count')
# 	monthNumber=[]
# 	totalOrders=[]
# 	for d in orders:
# 		monthNumber.append(calendar.month_name[d['month']])
# 		totalOrders.append(d['count'])
# 	return render(request, 'user/dashboard.html',{'monthNumber':monthNumber,'totalOrders':totalOrders})



# # My Orders
# def my_orders(request):
# 	orders=CartOrder.objects.filter(user=request.user).order_by('-id')
# 	return render(request, 'user/orders.html',{'orders':orders})



# # Order Detail
# def my_order_items(request,id):
# 	order=CartOrder.objects.get(pk=id)
# 	orderitems=CartOrderItems.objects.filter(order=order).order_by('-id')
# 	return render(request, 'user/order-items.html',{'orderitems':orderitems})



# # Wishlist
# def add_wishlist(request):
# 	pid=request.GET['product']
# 	product=Product.objects.get(pk=pid)
# 	data={}
# 	checkw=Wishlist.objects.filter(product=product,user=request.user).count()
# 	if checkw > 0:
# 		data={
# 			'bool':False
# 		}
# 	else:
# 		wishlist=Wishlist.objects.create(
# 			product=product,
# 			user=request.user
# 		)
# 		data={
# 			'bool':True
# 		}
# 	return JsonResponse(data)

# # My Wishlist
# def my_wishlist(request):
# 	wlist=Wishlist.objects.filter(user=request.user).order_by('-id')
# 	return render(request, 'user/wishlist.html',{'wlist':wlist})

# # My Reviews
# def my_reviews(request):
# 	reviews=ProductReview.objects.filter(user=request.user).order_by('-id')
# 	return render(request, 'user/reviews.html',{'reviews':reviews})

# # My AddressBook
# def my_addressbook(request):
# 	addbook=UserAddressBook.objects.filter(user=request.user).order_by('-id')
# 	return render(request, 'user/addressbook.html',{'addbook':addbook})

# # Save addressbook
# def save_address(request):
# 	msg=None
# 	if request.method=='POST':
# 		form=AddressBookForm(request.POST)
# 		if form.is_valid():
# 			saveForm=form.save(commit=False)
# 			saveForm.user=request.user
# 			if 'status' in request.POST:
# 				UserAddressBook.objects.update(status=False)
# 			saveForm.save()
# 			msg='Data has been saved'
# 	form=AddressBookForm
# 	return render(request, 'user/add-address.html',{'form':form,'msg':msg})

# # Activate address
# def activate_address(request):
# 	a_id=str(request.GET['id'])
# 	UserAddressBook.objects.update(status=False)
# 	UserAddressBook.objects.filter(id=a_id).update(status=True)
# 	return JsonResponse({'bool':True})

# # Edit Profile
# def edit_profile(request):
# 	msg=None
# 	if request.method=='POST':
# 		form=ProfileForm(request.POST,instance=request.user)
# 		if form.is_valid():
# 			form.save()
# 			msg='Data has been saved'
# 	form=ProfileForm(instance=request.user)
# 	return render(request, 'user/edit-profile.html',{'form':form,'msg':msg})

# # Update addressbook
# def update_address(request,id):
# 	address=UserAddressBook.objects.get(pk=id)
# 	msg=None
# 	if request.method=='POST':
# 		form=AddressBookForm(request.POST,instance=address)
# 		if form.is_valid():
# 			saveForm=form.save(commit=False)
# 			saveForm.user=request.user
# 			if 'status' in request.POST:
# 				UserAddressBook.objects.update(status=False)
# 			saveForm.save()
# 			msg='Address has been saved'
# 	form=AddressBookForm(instance=address)
# 	return render(request, 'user/update-address.html',{'form':form,'msg':msg})

# @csrf_exempt
# def payment_done(request):
# 	returnData=request.POST
# 	return render(request, 'payment-success.html',{'data':returnData})


# @csrf_exempt
# def payment_canceled(request):
# 	return render(request, 'payment-fail.html')



# def checkout(request):
#     categories = Category.objects.all()
#     context = {'categories': categories}
#     return render(request, 'checkout.html', context)


# def terms(request):
#     categories = Category.objects.all()
#     context = {'categories': categories}
#     return render(request, 'terms.html', context)



def contact(request):

#     categories = Category.objects.all()
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         message = request.POST['message']
#         message_body = f'''Hey, I am {name}.My phone number is {phone}.

#         {message}
#         '''
#         # send an email
#         send_mail(
#             f'Message from {name} ',
#             message_body,
#             email,
#             ['testerwebsite007@gmail.com'],
#             fail_silently=False,
#         )
#         context = {'name': name, 'categories': categories}

#     else:
#         context = {'categories': categories}
    context = {}
    return render(request, 'home_app/contact.html', context)

