from django.urls import path
from . import views

urlpatterns = [
    # main page
    path('', views.app, name='app'),

    # Individual product
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),

    # Individual category​
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
]
