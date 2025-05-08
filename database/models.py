# models.py

class Product:
    def __init__(self, title, price, link_of_product, condition_of_product=None, shipping=None, seller_info=None):
        self.title = title
        self.price = price
        self.link = link_of_product
        self.condition = condition_of_product
        self.shipping = shipping
        self.seller_info = seller_info
