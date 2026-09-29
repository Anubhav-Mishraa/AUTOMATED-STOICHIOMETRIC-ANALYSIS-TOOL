# Project Statement: Automated Stoichiometric Analysis Tool

## Problem Statement
Calculating molar masses and balancing chemical equations are foundational tasks in chemistry, yet they are highly prone to human arithmetic errors when done manually. Students and researchers frequently waste valuable time verifying stoichiometric coefficients rather than focusing on the core chemical concepts and laboratory applications. 

## Scope of the Project
This project provides a robust, terminal-based software solution to automate basic stoichiometric tasks. The scope is strictly defined to handle the mathematical computation of total molecular mass for user-defined chemical compounds and the automated stoichiometric balancing of standard 3-compound reactions (synthesis and decomposition). It relies on a local JSON database of atomic weights and outputs a persistent text log of all successful calculations. 

## Target Users
* **Chemistry Students:** To verify homework calculations and practice understanding the Law of Conservation of Mass.
* **Educators:** To quickly generate balanced equation examples for classroom demonstrations.
* **Lab Technicians:** To rapidly compute molar masses required for mixing standard chemical solutions.

## High-Level Features
1. **Interactive CLI Prompt:** A user-friendly terminal interface that guides the user through data entry with robust error handling for invalid data types.
2. **JSON Database Integration:** Decouples hardcoded atomic weights from the system logic, allowing the `periodic_table.json` file to be updated or expanded without altering the core Python scripts.
3. **Algorithmic Balancing Engine:** An iterative search algorithm that tests coefficient combinations to mathematically prove the conservation of mass across reactants and products.
4. **File I/O Logging:** Automatic appending of computed molecular masses into a local `chemistry_history.txt` file for session tracking.