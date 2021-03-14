# this is a website I am prototyping for a friends Business. 

## want to check out the site?
check the current state of the site.
https://acrotrainer.herokuapp.com/

### what works so far...
admin can add or delete products with photos they upload.


admin can add digital or physical products to page. if product is digital no address is required or saved to backend. if product requires shipping completed orders are saved to backend with shipping address. 


a logged in user can add items to cart.


the cart icon updates to let user know how many items are in the cart.


logged in user can see items in cart and prices in cart update accordingly.


logged in user can checkout. price and items are sent to backend.
guest has same capabilities as logged in user.

once order is completed cart is cleared.


a user can checkout with paypal.

paypal button does not show up in demo. it is hidden until I can get an SSL certificate for the site.


### initial setup:
this is a Django application in a Docker container with a postgres database that will be hosted off of heroku where the app will be launched.

### testing:
will test forms, models, urls, and views to ensure app runs smoothly and continues working while updates are being made.

