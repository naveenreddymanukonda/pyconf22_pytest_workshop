class Order:

    def __init__(self, product, quantity):
        self._product = product
        self._quantity = quantity
        self._filled = False

    def fill(self, warehouse):
        has_inventry = warehouse.has_inventory(
            self._product, 
            self._quantity
        )
        if has_inventry:
            warehouse.remove(self._product, self._quantity)
            self._filled = True

    def is_filled(self):
        return self._filled