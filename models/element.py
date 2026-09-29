

class Element:
    def __init__(self, symbol, atomic_weight, count):
        self.symbol = symbol
        self.atomic_weight = atomic_weight
        self.count = count
        
    def get_total_weight(self):
        return self.atomic_weight * self.count