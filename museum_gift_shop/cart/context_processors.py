from .cart import Cart

# 上下文处理器的作用是将购物车对象添加到每个模板的上下文中。这样，无论哪个视图函数渲染了模板，
# 模板都可以访问购物车对象，而不需要在每个视图函数中手动将购物车对象添加到模板的上下文中。
def cart(request):

    return {'cart': Cart(request)}



