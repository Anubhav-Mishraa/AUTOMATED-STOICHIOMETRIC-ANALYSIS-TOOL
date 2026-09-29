def save_calculation(mol_name, total_mass):
    try:
        # 'a' mode appends to the file instead of overwriting previous saves
        with open("chemistry_history.txt", "a") as file:
            file.write(f"Molecule: {mol_name} | Mass: {total_mass:.2f} g/mol\n")
        print("[+] Successfully saved to chemistry_history.txt")
    except Exception as e:
        print(f"[-] Error saving file: {e}")