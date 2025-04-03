# -Gestion D'un Inventaire de Produits :
• Afficher un menu principal avec différentes options. 
• Gérer un inventaire de produits (ajout, suppression, affichage). 
• Enregistrer les produits dans un fichier texte (.txt) et un fichier CSV (.csv) avec 
séparateur "," ou ";". 
• Lire les produits à partir d'un fichier texte ou CSV. 
• Rechercher un produit par son ID ou son nom. 
• Afficher les produits disponibles et ceux en rupture de stock.
1. Menu Principal : L’application doit afficher un menu permettant de : 
1. Afficher tous les produits. 
2. Ajouter un nouveau produit. 
3. Supprimer un produit. 
4. Rechercher un produit par ID. 
5. Rechercher un produit par nom. 
6. Enregistrer l'inventaire dans un fichier texte (.txt). 
7. Enregistrer l'inventaire dans un fichier CSV (.csv). 
8. Charger l'inventaire depuis un fichier texte (.txt). 
9. Charger l'inventaire depuis un fichier CSV (.csv). 
10. Quitter le programme. 
L’utilisateur doit pouvoir saisir son choix, et l’application doit exécuter l’action correspondante. 
2. Gestion des Produits : Chaque produit doit être stocké sous forme de dictionnaire et 
l’ensemble des produits dans une liste de dictionnaires. Chaque produit est caractérisé 
par : 
o ID 
o Nom 
o Quantité 
o Prix unitaire 
o Statut (Disponible ou Rupture de stock) 
3. Fonctions à implémenter : 
o Afficher tous les produits : Affiche tous les produits de l'inventaire. 
o Ajouter un produit : Permet à l'utilisateur d'ajouter un nouveau produit avec 
un ID unique, un nom, une quantité et un prix unitaire. Le statut est déterminé 
automatiquement en fonction de la quantité (Disponible si quantité > 0, sinon 
Rupture de stock). 
o Supprimer un produit : Permet à l'utilisateur de supprimer un produit en 
utilisant son ID. 
o Rechercher un produit par ID : Permet à l'utilisateur de rechercher un produit 
par son ID et affiche ses détails. 
o Rechercher un produit par nom : Permet à l'utilisateur de rechercher un 
produit par son nom et affiche ses détails. 
o Enregistrer l'inventaire dans un fichier texte : Enregistre la liste des produits 
dans un fichier texte (.txt). 
o Enregistrer l'inventaire dans un fichier CSV : Enregistre la liste des produits 
dans un fichier CSV (.csv) avec séparateur "," ou ";". 
o Charger l'inventaire depuis un fichier texte : Charge la liste des produits à 
partir d'un fichier texte (.txt). 
o Charger l'inventaire depuis un fichier CSV : Charge la liste des produits à 
partir d'un fichier CSV (.csv). 
4. Gestion des fichiers : 
o Utiliser la clause with pour lire et écrire dans un fichier texte. 
o Le fichier doit contenir une ligne par produit, avec les informations séparées par 
des virgules (CSV).
