class Product:
    def __init__(self, name):
        selfName = name
    def __init__(self, price):
        selfPrice = price
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_product_info(self):
        return "Product: (self.name), Price: (self.price)"