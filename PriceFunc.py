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


