#sp23-bai-042 ,#sp23-bai-037

class OutofStockError(Exception):
    def __init__(self, message = "out of stock"):
        self.message = message
        super().__init__(self.message)
class Product:
    def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

    def get_price(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity can't be Zero!")
        price = self.price * quantity
        if quantity >= 10:
            discount = price * (10/100)
            price = price - discount
            return price

        elif quantity >= 100:
            discount = price * (20/100)
            price = price - discount
            return price


    def make_purchase(self, quantity):
      if quantity > self.amount:
          raise OutofStockError(f"Quantity {quantity} is not in stock")
      else:
          self.amount = self.amount - quantity
          price = self.get_price(quantity=quantity)
          print(price)
      
Prod = Product("Bag", 25, 1000)
try:
    Prod.make_purchase(32)
except OutofStockError as exception:
    print(exception)
