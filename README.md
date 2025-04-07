# 🗃️ Inventory Management System - Python Project

This repository contains a Python-based inventory management application developed as part of the "Programmation Python" coursework for the academic year 2024–2025.

## 📚 Project Description

The goal of this project is to implement a simple yet functional inventory management system using core Python programming concepts such as:

- Control flow (if, elif, else)
- Loops (`for`, `while`)
- Functions (with parameters, return values, default values)
- File handling (`.txt` and `.csv`)
- Data structures (lists and dictionaries)

## 🛠 Features

The application provides a menu-driven interface for performing the following tasks:

1. Display all products
2. Add a new product
3. Delete a product
4. Search for a product by ID
5. Search for a product by name
6. Save inventory to a text file (`.txt`)
7. Save inventory to a CSV file (`.csv`)
8. Load inventory from a text file (`.txt`)
9. Load inventory from a CSV file (`.csv`)
10. Exit the application

Each product is represented by the following attributes:

- `ID`: Unique identifier
- `Name`: Product name
- `Quantity`: Stock quantity
- `Unit Price`: Price per unit
- `Status`: Automatically determined based on quantity (`Disponible` if > 0, otherwise `Rupture de stock`)

## 💾 File Management

- Products can be saved and loaded from `.txt` or `.csv` files.
- CSV files use `,` or `;` as separators.
- File operations use Python's `with` statement for better handling and safety.

## 👨‍🏫 Supervised by

- **Responsible Instructor**: Ines KAMOUN FOURATI
- **TP Instructors**: Marwa LOUKIL, Amal BOUDAYA, Yosr GHOZZI, Rahma GHORBEL, Rahme MAALEJ, Sirine MNEJJA, Lassaad ZAWAY

## 👨‍💻 How to Run

1. Make sure Python 3.x is installed.
2. Open the project in PyCharm or any Python IDE.
3. Run the script `Gestion_Inventaire.py`.
4. Follow the on-screen menu instructions.

## 📁 Example Run

```text
*** Bienvenue dans la Gestion de l'Inventaire ***

1. Afficher tous les produits
2. Ajouter un nouveau produit
...
10. Quitter

Entrez votre choix : 2

Entrez le nom du produit : Laptop
Entrez la quantité : 10
Entrez le prix unitaire : 1200
=> Le produit a été ajouté avec succès !
