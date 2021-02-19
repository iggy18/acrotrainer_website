from django.test import SimpleTestCase
from django.urls import reverse, resolve
from acrotrainer.views import store, cart, checkout

class TestUrls(SimpleTestCase):
    def test_store_url_is_resolved(self):
        url = reverse('store')
        print(resolve(url))
        self.assertEquals(resolve(url).func, store)

    def test_cart_url_is_resolved(self):
        url = reverse('cart')
        print(resolve(url))
        self.assertEquals(resolve(url).func, cart)

    def test_checkout_url_is_resolved(self):
        url = reverse('checkout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, checkout)