class EquationBalancer:
    def __init__(self, reactants, products):
        self.reactants = reactants  # List of Molecule objects
        self.products = products    # List of Molecule objects

    def _get_atom_counts(self, molecules, coefficients):
        """Calculates total atoms for a given side of the equation."""
        counts = {}
        for i in range(len(molecules)):
            mol = molecules[i]
            coeff = coefficients[i]
            for el in mol.elements:
                if el.symbol in counts:
                    counts[el.symbol] += el.count * coeff
                else:
                    counts[el.symbol] = el.count * coeff
        return counts

    def auto_balance(self):
        """
        Brute-force algorithm that tests coefficients from 1 to 15.
        Only works for exactly 3 total compounds (2 reactants/1 product OR 1 reactant/2 products).
        """
        if len(self.reactants) + len(self.products) != 3:
            return False, "This feature only supports exactly 3 compounds."

        # Test every combination of coefficients (c1, c2, c3) from 1 to 15
        for c1 in range(1, 16):
            for c2 in range(1, 16):
                for c3 in range(1, 16):
                    
                    if len(self.reactants) == 2:
                        r_coeffs = [c1, c2]
                        p_coeffs = [c3]
                    else:
                        r_coeffs = [c1]
                        p_coeffs = [c2, c3]
                        
                    r_counts = self._get_atom_counts(self.reactants, r_coeffs)
                    p_counts = self._get_atom_counts(self.products, p_coeffs)
                    
                    # If the dictionaries match exactly, mass is conserved!
                    if r_counts == p_counts:
                        return True, (r_coeffs, p_coeffs)
                        
        return False, "Could not balance with coefficients under 15."