import json
from models.element import Element
from models.molecule import Molecule
from models.balancer import EquationBalancer
from utils.storage import save_calculation

# read the atomic weights from our local json database
def load_periodic_table():
    with open("data/periodic_table.json", "r") as file:
        return json.load(file)

def build_molecule(table, prompt_name):
    
    mol_name = input(f"\n{prompt_name} (e.g., Water, CO2): ")
    new_mol = Molecule(mol_name)

    # keep asking for elements until the user types 'done'
    while True:
        symbol = input("  Enter element symbol (or 'done'): ").strip()
        if symbol.lower() == 'done':
            break
        if symbol in table:
            try:
                count = int(input(f"  How many {symbol} atoms? "))
                
                new_mol.add_element(Element(symbol, table[symbol]["mass"], count))
            except ValueError:
                print("  [-] Please enter a valid number.")
        else:
            print("  [-] Element not found. Check capitalization.")
    return new_mol

def format_equation(reactants, products, r_coeffs, p_coeffs):
    
    r_str = " + ".join([f"{c} {m.name}" for c, m in zip(r_coeffs, reactants)])
    p_str = " + ".join([f"{c} {m.name}" for c, m in zip(p_coeffs, products)])
    return f"{r_str} -> {p_str}"

def main():
    table = load_periodic_table()
    
    while True:
        print("\n" + "="*46)
        print("   AUTOMATED STOICHIOMETRIC ANALYSIS TOOL")
        print("="*46)
        print("1. Calculate Molecular Mass")
        print("2. Auto-Balance 3-Compound Equation")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ")
        
        if choice == '1':
            my_molecule = build_molecule(table, "Enter molecule name")

            # calculate the total mass before finding percentages
            mass = my_molecule.calculate_total_mass()
            if mass > 0:
                print(f"\n[+] Total Mass for {my_molecule.name}: {mass:.2f} g/mol")
                print("Percentage Composition:")
                percents = my_molecule.get_percentages(mass)
                for sym, p in percents.items():
                    print(f"  - {sym}: {p:.2f}%")
                save_calculation(my_molecule.name, mass)
                
        elif choice == '2':
            print("\n--- Equation Type ---")
            print("A. Synthesis (2 Reactants -> 1 Product)")
            print("B. Decomposition (1 Reactant -> 2 Products)")
            eq_type = input("Choose A or B: ").strip().upper()
            
            reactants = []
            products = []

            # setup the lists based on the type of reaction
            if eq_type == 'A':
                reactants.append(build_molecule(table, "Enter Reactant 1"))
                reactants.append(build_molecule(table, "Enter Reactant 2"))
                products.append(build_molecule(table, "Enter Product 1"))
            elif eq_type == 'B':
                reactants.append(build_molecule(table, "Enter Reactant 1"))
                products.append(build_molecule(table, "Enter Product 1"))
                products.append(build_molecule(table, "Enter Product 2"))
            else:
                print("[-] Invalid choice. Returning to menu.")
                continue
                
            print("\nCalculating balance...")
            balancer = EquationBalancer(reactants, products)
            success, result = balancer.auto_balance()
            
            if success:
                r_coeffs, p_coeffs = result
                final_eq = format_equation(reactants, products, r_coeffs, p_coeffs)
                print(f"\n[+] SUCCESS! Balanced Equation:")
                print(f"    {final_eq}")
            else:
                print(f"\n[-] FAILED: {result}")
                
        elif choice == '3':
            print("Exiting program. Best of luck with your project!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()