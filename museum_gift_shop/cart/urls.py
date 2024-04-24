from django.urls import path
from . import views

urlpatterns = [
    # redirect to cart page
    path('', views.cart_summary, name='cart-summary'),

    # no pages, these are going to be handled with Ajax(异步javascript)
    path('add/', views.cart_add, name='cart-add'),
    path('delete/', views.cart_delete, name='cart-delete'),
    path('update/', views.cart_update, name='cart-update'),
]
