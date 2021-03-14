from django.shortcuts import render
from .models import Customer, Product, Order, OrderItem, ShippingAddress
from django.http import JsonResponse
from .helpers import cookie_maker, cart_data, guest_order
import json
import datetime

def store(request):
    data = cart_data(request)
    cartItems = data['cartItems']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    data = cart_data(request)
    cartItems = data['cartItems']
    order = data['order']
    items =data['items']
    context = {'items': items, 'order': order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    data = cart_data(request)
    cartItems = data['cartItems']
    order = data['order']
    items =data['items']
    context = {'items': items, 'order': order, 'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('action', action)
    print('product', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem. quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('item has been added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    print(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        if order.hide_shipping_address == True:
            ShippingAddress.objects.create(
                customer = customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            ) 
    else:
        customer, order = guest_order(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    if order.hide_shipping_address == True:
        ShippingAddress.objects.create(
            customer = customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        ) 

    return JsonResponse('Payment complete!', safe=False)