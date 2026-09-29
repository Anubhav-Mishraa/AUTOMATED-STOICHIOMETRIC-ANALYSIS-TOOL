# AUTOMATED STOICHIOMETRY ANALYSIS TOOL

## Description of the Project
Automated Stoichiometric Analysis Tool is a command-line tool designed to help you in computational chemistry by allowing you to
build molecules interactively, calculate an exact molar mass of a compound using an isolated database, and balance 3-compound equations using an iterative verification algorithm.

## Features of the Project
Build molecules element by element in a modular fashion. Compute the exact molecular mass of desired compound. Auto-balance synthesis (2 reactants -> 1 product) and decomposition (1 reactant -> 2 products) chemical equations using a brute-force iterative algorithm. Store the working calculations in history.

## Technologies/Tools Used
Python3, Object-oriented Programming paradigm, JSON, File I/O

## How to Set Up the Project
Install dependencies (if any): `pip install -r requirements.txt`
Clone this repository to a folder on your local machine : `git clone https://github.com/Anubhav-Mishraa/AUTOMATED-STOICHIOMETRIC-ANALYSIS-TOOL`
Open folder in terminal and activate venv : `cd AUTOMATED-STOICHIOMETRIC-ANALYSIS-TOOL`
Finally, run the program using the following command
```bash
python main.py
```
Note: If you are on a Mac or a Linux system, or if you have python3 installed on windows, use `python3 main.py` instead.
## How to Test the Project

Run the program and go to the Auto-Balance 3-Compound Equation menu by selecting option 2, and then select option A for synthesis
Type out the elements and their stoichiometric coefficient for Reactant 1, hit enter after each
Type `done` when you are finished with Reactant 1. You can also type out the elements and their stoichiometric coefficient for Reactant 2, and then hit enter after each
Type `done` when you are finished with Reactant 2. Finally, type out the elements and their stoichiometric coefficient for Product 1, and then hit enter after each. The program should give you the following output `2 H + 1 O -> 2 Water`
1. Run the program
2. Select option 2 to go to the Auto-Balance 3-Compound Equation menu
3. Select option A for synthesis
4. For Reactant 1, type `H` and hit enter, then type `2` and hit enter. Then type `done`.
5. For Reactant 2, type `O` and hit enter, then type `2` and hit enter. Then type `done`.
6. For Product 1, type `H` and hit enter, then type `2` and hit enter. Then type `O` and hit enter, then type `1` and hit enter. Then type `done`.

