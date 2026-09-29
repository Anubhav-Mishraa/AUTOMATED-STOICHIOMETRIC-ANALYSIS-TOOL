# Automated Stoichiometric Analysis Tool

## Overview of the Project
The Automated Stoichiometric Analysis Tool is a command-line utility built to assist in computational chemistry. It allows users to dynamically build molecule objects, compute accurate molar masses based on an isolated atomic database, and automatically balance 3-compound chemical equations using an iterative verification algorithm.

## Features
* **Modular Molecular Building:** Interactively construct complex molecules element by element.
* **Molar Mass Computation:** Instantly calculates total molecular weight (g/mol) using standard atomic masses.
* **Automated Equation Balancer:** Uses a brute-force iterative algorithm to balance synthesis (2 reactants → 1 product) and decomposition (1 reactant → 2 products) reactions.
* **Data Persistence:** Automatically saves successful calculations to a local text file (`chemistry_history.txt`) for later review.

## Technologies/Tools Used
* **Language:** Python 3.x
* **Architecture:** Object-Oriented Programming (OOP)
* **Storage:** JSON (for the periodic table database) and standard File I/O (for calculation history).
* **Dependencies:** None. Built entirely using Python's standard library.

## Steps to Install & Run the Project
1. Clone the repository to your local machine:
   `git clone https://github.com/your-username/chemistry-project.git`
2. Navigate into the project directory:
   `cd chemistry-project`
3. Execute the program via the terminal:
   `python main.py` *(Note: Use `python3 main.py` on Mac/Linux or if specifically configured on Windows)*.

## Instructions for Testing
To verify the system is working correctly, run the application and select **Option 2** (Auto-Balance 3-Compound Equation) from the main menu. 
1. Choose **A** for Synthesis.
2. **Reactant 1:** Type `H`, press enter, type `2`, press enter. Type `done`.
3. **Reactant 2:** Type `O`, press enter, type `2`, press enter. Type `done`.
4. **Product 1:** Type `H`, press enter, type `2`, press enter. Type `O`, press enter, type `1`, press enter. Type `done`.
5. The system should successfully output: `2 H + 1 O -> 2 Water`.

## Screenshots
*(Note for submission: Take 1-2 screenshots of your VS Code terminal running the successful test above, save them in your repository, and add the image links here).*