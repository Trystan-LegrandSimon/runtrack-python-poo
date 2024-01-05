#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

class Forme:
    
    def aire(self):
        print("Calcul de l'aire dans la classe Forme.")
        return 0

class Rectangle(Forme):
    
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        aire_rectangle = self.largeur * self.hauteur
        print(f"Calcul de l'aire dans la classe Rectangle : {aire_rectangle} m²")
        return aire_rectangle

# Instanciation de la classe Rectangle
rectangle1 = Rectangle(largeur = 4, hauteur = 5)

# Appel de la méthode aire de la classe Rectangle
resultat_aire = rectangle1.aire()