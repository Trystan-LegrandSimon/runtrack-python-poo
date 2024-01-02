#!/usr/local/bin/python3.12

class Produit:
    
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        infos = f"Nom : {self.nom},\nPrix HT : {self.prixHT}, \nTVA : {self.TVA}%"
        print(infos)

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

# Création de plusieurs produits
produit1 = Produit("Livre", 15.0, 5)
produit2 = Produit("Ordinateur", 1000.0, 20)

# Calcul des prix TTC et affichage des informations des produits
for produit in [produit1, produit2]:
    print()
    produit.afficher()
    print(f"Prix TTC : {produit.calculerPrixTTC()}")


# Modification du nom et du prix de chaque produit
produit1.modifierNom("Roman")
produit1.modifierPrix(12.5)

produit2.modifierNom("Laptop")
produit2.modifierPrix(950.0)

# Affichage des nouvelles informations des produits
for produit in [produit1, produit2]:
    print()
    produit.afficher()
    print(f"Nouveau prix TTC : {produit.calculerPrixTTC()}")
    
print()