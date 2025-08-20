class CoffeeMenu:
  def __init__(self):
    self.menu = {
      'espresso': 2.50,
      'latte': 2.75,
      'cappuccino': 3.20,
      'americano': 2.70
    }
    def get_price(self, name):
        return self.menu.get(name.lower())
    def add_item(self, item, price):
        self.menu[item.lower()] = price