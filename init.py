import csv
import random

def charger_csv():
    inventaire = []
    try:
        with open("inventaire.csv", "r", newline='', encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader, None)
            for line in csv_reader:
                if len(line) < 5:
                    continue
                try:
                    produit = {
                        "ID": int(line[0]),
                        "Nom": line[1],
                        "Quantité": int(line[2]),
                        "Prix": float(line[3]),
                        "Statut": line[4],
                    }
                    inventaire.append(produit)
                except (ValueError, IndexError):
                    continue
    except FileNotFoundError:
        inventaire = []
    return inventaire

inventaire = charger_csv()


def afficher_menu():
    """Affiche le menu principal"""
    print("\n" + "="*50)
    print("*** Gestion de l'Inventaire ***".center(50))
    print("="*50)
    print("1 . Afficher tous les produits")
    print("2 . Ajouter un nouveau produit")
    print("3 . Supprimer un produit")
    print("4 . Rechercher un produit par nom")
    print("5 . Rechercher un produit par ID")
    print("6 . Mettre à jour le stock")
    print("7 . Enregistrer l'inventaire (fichier texte)")
    print("8 . Enregistrer l'inventaire (fichier CSV)")
    print("9 . Charger l'inventaire (fichier texte)")
    print("10. Charger l'inventaire (fichier CSV)")
    print("11. Quitter")
    print("="*50)

def afficher_produits():
    """Affiche tous les produits de l'inventaire"""
    if not inventaire:
        print("\nL'inventaire est vide.")
        return
    
    print("\n" + "-" * 80)
    print("LISTE COMPLÈTE DES PRODUITS".center(80))
    print("-" * 80)

    
    print(f"{'ID':^20} {'Nom':<25} {'Quantité':^10} {'Prix':^10} {'Statut':^15}")
    print("-" * 80)

    
    for produit in inventaire:
        print(f"{produit['ID']:^20} {produit['Nom']:<25} {produit['Quantité']:^10} {produit['Prix']:^10.2f} {produit['Statut']:^15}")

    print("-" * 80)
    return

def generer_id() -> int:
    """Génère un ID unique pour un nouveau produit"""
    return random.randint(1, 100000000000000)

def verifier_id_existe(id: int) -> bool:
    """Vérifie si un ID existe déjà dans l'inventaire"""
    return any(produit["ID"] == id for produit in inventaire)

def saisir_entier(message: str, min_val=None) -> int:
    """Demande à l'utilisateur de saisir un entier valide"""
    while True:
        try:
            valeur = int(input(message))
            if min_val is not None and valeur < min_val:
                print(f"La valeur doit être supérieure ou égale à {min_val}")
                continue
            return valeur
        except ValueError:
            print("Veuillez entrer un nombre entier valide!")

def saisir_reel(message: str, min_val=None) -> float:
    """Demande à l'utilisateur de saisir un réel valide"""
    while True:
        try:
            valeur = float(input(message))
            if min_val is not None and valeur < min_val:
                print(f"La valeur doit être supérieure ou égale à {min_val}")
                continue
            return valeur
        except ValueError:
            print("Veuillez entrer un nombre valide!")

def ajouter_produit():
    """Ajoute un nouveau produit à l'inventaire"""
    print("\n" + "="*50)
    print("AJOUT D'UN NOUVEAU PRODUIT".center(50))
    print("="*50)
    
    nouveau_produit = {}
    
    # Génération d'un ID unique
    nouveau_produit["ID"] = generer_id()
    while verifier_id_existe(nouveau_produit["ID"]):
        nouveau_produit["ID"] = generer_id()
    
    nouveau_produit["Nom"] = input("Nom du produit: ").strip()
    nouveau_produit["Quantité"] = saisir_entier("Quantité: ", 0)
    nouveau_produit["Prix"] = saisir_reel("Prix unitaire: ", 0)
    nouveau_produit["Statut"] = "Disponible" if nouveau_produit["Quantité"] > 0 else "Indisponible"
    
    inventaire.append(nouveau_produit)
    print(f"\nProduit '{nouveau_produit['Nom']}' ajouté avec succès (ID: {nouveau_produit['ID']})!")

def supprimer_produit():
    """Supprime un produit de l'inventaire"""
    if not inventaire:
        print("\nL'inventaire est vide. Aucun produit à supprimer.")
        return
    
    print("\n" + "="*50)
    print("SUPPRESSION D'UN PRODUIT".center(50))
    print("="*50)
    
    id = saisir_entier("ID du produit à supprimer: ")
    
    for i, produit in enumerate(inventaire):
        if produit["ID"] == id:
            nom_produit = produit["Nom"]
            del inventaire[i]
            print(f"\nProduit '{nom_produit}' (ID: {id}) supprimé avec succès!")
            return
    
    print(f"\nAucun produit trouvé avec l'ID {id}.")

def rechercher_par_nom():
    """Recherche des produits par nom"""
    if not inventaire:
        print("\nL'inventaire est vide. Aucun produit à rechercher.")
        return
    
    print("\n" + "="*50)
    print("RECHERCHE PAR NOM".center(50))
    print("="*50)
    
    terme = input("Entrez le nom ou une partie du nom à rechercher: ").strip().lower()
    resultats = [p for p in inventaire if terme in p["Nom"].lower()]
    
    if not resultats:
        print("\nAucun produit trouvé avec ce critère.")
        return
    
    print(f"\n{len(resultats)} produit(s) trouvé(s):")
    print("-"*80)
    print(f"{'ID':^20} {'Nom':<25} {'Quantité':^10} {'Prix':^10} {'Statut':^15}")
    print("-"*80)
    
    for produit in resultats:
        print(f"{produit['ID']:^20} {produit['Nom']:<25} {produit['Quantité']:^10} {produit['Prix']:^10.2f} {produit['Statut']:^15}")
    print("-"*80)

def rechercher_par_id():
    """Recherche un produit par son ID"""
    if not inventaire:
        print("\nL'inventaire est vide. Aucun produit à rechercher.")
        return
    
    print("\n" + "="*50)
    print("RECHERCHE PAR ID".center(50))
    print("="*50)
    
    id = saisir_entier("ID du produit à rechercher: ")
    
    for produit in inventaire:
        if produit["ID"] == id:
            print("\n" + "="*50)
            print("DÉTAILS DU PRODUIT".center(50))
            print("="*50)
            print(f"ID: {produit['ID']}")
            print(f"Nom: {produit['Nom']}")
            print(f"Quantité: {produit['Quantité']}")
            print(f"Prix unitaire: {produit['Prix']:.2f}")
            print(f"Statut: {produit['Statut']}")
            print("="*50)
            return
    
    print(f"\nAucun produit trouvé avec l'ID {id}.")

def mettre_a_jour_stock():
    """Met à jour la quantité en stock d'un produit"""
    if not inventaire:
        print("\nL'inventaire est vide. Aucun produit à modifier.")
        return
    
    print("\n" + "="*50)
    print("MISE À JOUR DU STOCK".center(50))
    print("="*50)
    
    id = saisir_entier("ID du produit à modifier: ")
    
    for produit in inventaire:
        if produit["ID"] == id:
            print(f"\nProduit actuel: {produit['Nom']}")
            print(f"Stock actuel: {produit['Quantité']}")
            
            modification = saisir_entier("Quantité à ajouter (nombre négatif pour retirer): ")
            nouveau_stock = produit["Quantité"] + modification
            
            if nouveau_stock < 0:
                print("\nAttention: Le stock ne peut pas être négatif!")
                print("Le stock sera mis à 0.")
                nouveau_stock = 0
            
            produit["Quantité"] = nouveau_stock
            produit["Statut"] = "Disponible" if nouveau_stock > 0 else "Indisponible"
            
            print("\nMise à jour effectuée avec succès!")
            print(f"Nouveau stock: {produit['Quantité']}")
            print(f"Nouveau statut: {produit['Statut']}")
            return
    
    print(f"\nAucun produit trouvé avec l'ID {id}.")

def enregistrer_texte():
    """Enregistre l'inventaire dans un fichier texte"""
    if not inventaire:
        print("\nL'inventaire est vide. Aucune donnée à enregistrer.")
        return
    
    with open("inventaire.txt", "w", encoding="utf-8") as f:
        f.write("="*80 + "\n")
        f.write("INVENTAIRE - LISTE DES PRODUITS".center(80) + "\n")
        f.write("="*80 + "\n\n")
        
        for produit in inventaire:
            f.write(f"ID: {produit['ID']}\n")
            f.write(f"Nom: {produit['Nom']}\n")
            f.write(f"Quantité: {produit['Quantité']}\n")
            f.write(f"Prix unitaire: {produit['Prix']:.2f}\n")
            f.write(f"Statut: {produit['Statut']}\n")
            f.write("-"*80 + "\n")
    
    print("\nInventaire enregistré avec succès dans 'inventaire.txt'")
    return

def enregistrer_csv():
    """Enregistre l'inventaire dans un fichier CSV"""
    if not inventaire:
        print("\nL'inventaire est vide. Aucune donnée à enregistrer.")
        return
    
    with open("inventaire.csv", "w", newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["ID", "Nom", "Quantité", "Prix", "Statut"])
        
        for produit in inventaire:
            writer.writerow([
                produit["ID"],
                produit["Nom"],
                produit["Quantité"],
                produit["Prix"],
                produit["Statut"]
            ])
    
    print("\nInventaire enregistré avec succès dans 'inventaire.csv'")
    return

def charger_texte():
    """Affiche le contenu du fichier texte"""
    try:
        with open("inventaire.txt", "r", encoding="utf-8") as f:
            print("\n" + "="*80)
            print("CONTENU DE INVENTAIRE.TXT".center(80))
            print("="*80)
            print(f.read())
    except FileNotFoundError:
        print("\nFichier 'inventaire.txt' introuvable!")
    return

def afficher_cvs():
    """Affiche le contenu du fichier CSV"""
    try:
        with open("inventaire.csv", "r", newline='', encoding="utf-8") as csv_file:
            print("\n" + "="*80)
            print("CONTENU DE INVENTAIRE.CSV".center(80))
            print("="*80)
            reader = csv.reader(csv_file)
            for row in reader:
                print(", ".join(row))
    except FileNotFoundError:
        print("\nFichier 'inventaire.csv' introuvable!")
    return

def quitter():
    """Quitte le programme"""
    enregistrer_csv()
    print("\nMerci d'avoir utilisé le système de gestion d'inventaire!")
    exit()
    return

def main():
    """Fonction principale du programme"""
    print("\n" + "="*50)
    print("SYSTÈME DE GESTION D'INVENTAIRE".center(50))
    print("="*50)
    global inventaire
    inventaire = charger_csv()
    while True:
        afficher_menu()
        
        try:
            choix = saisir_entier("\nVotre choix (1-11): ", 1)
            
            if choix == 1:
                afficher_produits()
            elif choix == 2:
                ajouter_produit()
            elif choix == 3:
                supprimer_produit()
            elif choix == 4:
                rechercher_par_nom()
            elif choix == 5:
                rechercher_par_id()
            elif choix == 6:
                mettre_a_jour_stock()
            elif choix == 7:
                enregistrer_texte()
            elif choix == 8:
                enregistrer_csv()
            elif choix == 9:
                charger_texte()
            elif choix == 10:
                afficher_cvs()
                
            elif choix == 11:
                
                quitter()
            else:
                print("\nChoix invalide. Veuillez sélectionner une option entre 1 et 11.")
        
        except ValueError:
            print("\nErreur: Veuillez entrer un nombre valide!")
        
        input("\nAppuyez sur Entrée pour continuer...")

