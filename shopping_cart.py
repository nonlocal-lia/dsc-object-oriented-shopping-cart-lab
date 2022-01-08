import numpy as np

class ShoppingCart:
    # write your code here
   def __init__(self, emp_discount=None):
      self.total = 0
      self.employee_discount = emp_discount
      self.items = []
   
   @property
   def total(self):
      return self._total

   @total.setter
   def total(self, value):
      self._total = value
   
   @property
   def employee_discount(self):
      return self._employee_discount

   @employee_discount.setter
   def employee_discount(self, emp_discount):
      self._employee_discount = emp_discount

   @property
   def items(self):
      return self._items

   @items.setter
   def items(self, item_list):
      self._items = item_list

   def add_item(self, name, price, quantity=1):        
      for i in range(quantity):
         self._items.append({'Name': name, 'Price': price})
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
            prices.append(item['Price'])
         return np.median(prices)
      else:
         return 0

   def apply_discount(self):
      if self.employee_discount:
         return self.total*(100 - self.employee_discount)/100
      else:
         return "Sorry, there is no discount to apply to your cart :("

   def void_last_item(self):
      voided = self.items.pop()
      self.total -= voided['Price']
      return self.total
      