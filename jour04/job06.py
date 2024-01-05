#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

class Vehicule:
    
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}")
        print(f"Modèle: {self.modele}")
        print(f"Année: {self.annee}")
        print(f"Prix: {self.prix} €")

    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    
    def __init__(self, marque, modele, annee, prix, portes = 4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")

    def demarrer(self):
        super().demarrer()
        print("La voiture démarre avec un son vrombissant !")


class Moto(Vehicule):
    
    def __init__(self, marque, modele, annee, prix, roues = 2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")

    def demarrer(self):
        super().demarrer()
        print("La moto démarre avec un rugissement !")


# Instanciation d'une voiture
voiture1 = Voiture(marque = "Mercedes", modele = "Classe A", annee = 2020, prix = 18500)
voiture1.informationsVehicule()
voiture1.demarrer()
print()

# Instanciation d'une moto
moto1 = Moto(marque = "Yamaha", modele = "1200 Vmax", annee = 1987, prix = 4500)
moto1.informationsVehicule()
moto1.demarrer()