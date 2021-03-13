import json
from . models import Customer, Product, Order, OrderItem, ShippingAddress

def cookie_maker(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    cart = json.loads(request.COOKIES['cart'])
    print('cart: ', cart)
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