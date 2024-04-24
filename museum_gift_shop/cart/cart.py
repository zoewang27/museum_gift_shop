from decimal import Decimal
from app.models import Product

# 使用 Cart 类来管理购物车的状态和数据
# cart: 保存了购物车的内容，是一个字典，键为商品的 ID，值为包含商品数量和价格的字典。
# 购物车的内容是存储在 session 中的，而不是直接存储在 Cart 类的属性中。Cart 类中的 self.cart 属性实际上是从 session 中获取的购物车内容的引用。
# 因此，当我们修改了购物车的内容（即修改了 self.cart），我们需要通知 Django session 对象已被修改，以便在请求结束后保存修改后的内容。

class Cart():

    # 购物车的内容会被存储在 self.session 中的一个特定的键下，通常是名为 'cart' 的键。
    def __init__(self, request):
    
        self.session = request.session   
        # Returning user - obtain his/her existing session    
        cart = self.session.get('session_key')
        # New user - generate a new session    
        if 'session_key' not in request.session: 
            cart = self.session['session_key'] = {}
        self.cart = cart


    def add(self, product, product_qty): 
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': product_qty}
        self.session.modified = True

    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True

    def update(self, product, qty):
        product_id = str(product)
        product_quantity = qty
        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_quantity
        self.session.modified = True

    # 计算总的数量，用于购物车的图标旁边全局显示
    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())

    # 根据product_id，获取对应的product数据，用在购物车页面
    def __iter__(self):
        all_product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=all_product_ids)
        cart = self.cart.copy()
    
        for product in products:
            cart[str(product.id)]['product'] = product
    
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['qty']
            yield item    

    # 计算总价格，用在购物车页面
    def get_total(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

