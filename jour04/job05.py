#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

import math

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

class Cercle(Forme):
    
    def __init__(self, rayon):
        self.radius = rayon

    def aire(self):
        aire_cercle = math.pi * self.radius**2
        print(f"Calcul de l'aire dans la classe Cercle : {aire_cercle:.2f} m²")
        return aire_cercle

# Instanciation de la classe Rectangle
rectangle1 = Rectangle(largeur = 4, hauteur = 5)

# Appel de la méthode aire de la classe Rectangle
resultat_aire_rectangle = rectangle1.aire()

# Instanciation de la classe Cercle
cercle1 = Cercle(rayon = 3)

# Appel de la méthode aire de la classe Cercle
resultat_aire_cercle = cercle1.aire()