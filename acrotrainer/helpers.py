import json
from . models import Customer, Product, Order, OrderItem, ShippingAddress

def cookie_maker(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    items = []
    order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
    cartItems = order['get_cart_items']
    for inventory in cart:
        try:
            cartItems += cart[inventory]['quantity']
            product = Product.objects.get(id=inventory)
            total = (product.price*cart[inventory]['quantity'])
            
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[inventory]['quantity']

            item = {
                'product':{
                    'id':product.id,
                    'name':product.name,
                    'price':product.price,
                    'image_handler': product.image_handler
                    },
                'quantity':cart[inventory]['quantity'],
                'get_total':total,
                }
            items.append(item)

            if product.digital == False:
                order['shipping'] = True
        except:
            pass
    return {'cartItems': cartItems, 'order':order, 'items':items}

def cart_data(request):
    if request.user.is_authenticated: 
        new_customer, created = Customer.objects.get_or_create(user=request.user, name=request.user.username, email=request.user.email)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookie_data = cookie_maker(request)
        cartItems = cookie_data['cartItems']
        order = cookie_data['order']
        items =cookie_data['items']
    return {'cartItems': cartItems, 'order':order, 'items': items}

def guest_order(request, data):
    name = data['form']['name']
    email = data['form']['email']
    cookie_data = cookie_maker(request)
    items = cookie_data['items']
    customer, created = Customer.objects.get_or_create(
        email=email, 
    )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )
    return customer, order