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



# create product object
# make purchases against different product quantities (make sure to run each test case)
# do not forget to handle exceptions
# print the remaining stock after each purchase