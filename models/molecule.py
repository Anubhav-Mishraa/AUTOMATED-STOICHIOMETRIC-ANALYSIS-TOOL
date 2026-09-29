class Molecule:
    def __init__(self, name):
        self.name = name
        self.elements = []
        
    def add_element(self, element_obj):
        self.elements.append(element_obj)
        
    def calculate_total_mass(self):
        total = 0
        for el in self.elements:
            total += el.get_total_weight()
        return total

    def get_percentages(self, total):
        # dictionary to hold symbol: percentage
        percent_dict = {}
        if total == 0:
            return percent_dict
            
        for el in self.elements:
            percent = (el.get_total_weight() / total) * 100
            percent_dict[el.symbol] = percent
        return percent_dict
