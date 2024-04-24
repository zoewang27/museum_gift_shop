from django.shortcuts import render

from .cart import Cart
from app.models import Product

from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def cart_summary(request):

    cart = Cart(request) #实例化了一个 Cart 对象，调用 Cart 类的构造函数 __init__。这是因为在每次实例化一个类的对象时，都会自动调用该类的构造函数来初始化对象的属性。
    return render(request, 'cart/cart-summary.html', {'cart':cart})



def cart_add(request):
  
    cart = Cart(request)
    #  POST 请求中获取商品ID和数量，并使用 Cart 类的 add 方法将商品添加到购物车中。
    if request.POST.get('action') == 'post':
    
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, product_qty=product_quantity)
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity}) #返回一个包含购物车中商品数量的 JSON 响应
    
    return response



def cart_delete(request):

    cart = Cart(request)
    # 从 POST 请求中获取要删除的商品ID，并使用 Cart 类的 delete 方法将商品从购物车中删除。
    if request.POST.get('action') == 'post':
    
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        cart_quantity = cart.__len__()
        cart_total = cart.get_total()
        response = JsonResponse({'qty':cart_quantity, 'total':cart_total})
    
    return response



def cart_update(request):

    cart = Cart(request)
    # 从 POST 请求中获取商品ID和新的数量，并使用 Cart 类的 update 方法更新购物车中相应商品的数量
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        cart.update(product=product_id, qty=product_quantity)
        cart_quantity = cart.__len__()
        cart_total = cart.get_total()
        response = JsonResponse({'qty':cart_quantity, 'total':cart_total})
    
    return response

