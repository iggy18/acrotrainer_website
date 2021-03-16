from django.urls import path
from . import views

urlpatterns =[
    path('', views.welcome, name='welcome'), 
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
    path('store/',views.store, name='store'), 
    path('cart/',views.cart, name='cart'),
    path('checkout/',views.checkout, name='checkout'),
    path('update_item/',views.updateItem, name='update_item'),
]

handler404 = views.handler404
