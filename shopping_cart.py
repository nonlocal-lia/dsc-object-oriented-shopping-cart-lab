import numpy as np

class ShoppingCart:
    # write your code here
    def __init__(self, total=0, emp_discount=None, items=[]):
      self.total = total
      self.employee_discount = emp_discount
      self.items = items
      self.item_prices = {}

    def add_item(self, name, price, quantity=1):
      self.item_prices[name] = price
      for i in range(quantity):
         self.items.append(name)
         self.total += price
      return self.total
       
    def mean_item_price(self):
      if len(self.items) != 0:
         return self.total / len(self.items)
      else:
         return 0

    def median_item_price(self):
      if len(self.items) != 0:
         prices = []
         for item in self.items:
            prices.append(self.item_prices[item])
         return np.median(prices)
      else:
         return 0

    def apply_discount(self):
      if self.employee_discount:
         return self.total*(100 -self.employee_discount)/100
      else:
         return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
      voided = self.items.pop()
      self.total -= self.item_prices[voided]
      return self.total
      