'''class Molecule:
    def __init__(self, name):
        """Creates a new, empty molecule with a given name."""
        self.name = name
        # We use a dictionary to store the element and how many atoms of it exist
        self.components = {}

    def add_element(self, element_object, count):
        """Adds an element and its atom count to the molecule."""
        self.components[element_object] = count

    def calculate_total_mass(self):
        """Loops through all added elements and calculates the total mass."""
        total = 0.0
        for element, count in self.components.items():
            total += element.mass * count
        return total

    def generate_report(self):
        """Creates a readable summary of the mass and percentages."""
        total_mass = self.calculate_total_mass()
        
        # If the molecule is empty, prevent a math error (dividing by zero)
        if total_mass == 0:
            return "This molecule has no elements yet."

        report = f"\n=== RESULTS FOR {self.name.upper()} ===\n"
        report += f"Total Molar Mass: {total_mass:.3f} g/mol\n"
        report += "Percentage Composition:\n"
        
        # Calculate the percentage for each element
        for element, count in self.components.items():
            mass_contribution = element.mass * count
            percentage = (mass_contribution / total_mass) * 100
            report += f"  - {element.name} ({element.symbol}): {percentage:.2f}%\n"
            
        return report'''


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