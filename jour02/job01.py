#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

'''
    Méthod Privée
'''

class Rectangle:
    
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Assesseurs (getters)
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs (setters)
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

# Créer un rectangle avec les valeurs initiales
mon_rectangle = Rectangle(0, 0)

# Afficher les valeurs initiales
print()
print("Valeur Initiale :")
print(f"Longueur initiale : {mon_rectangle.get_longueur()}")
print(f"Largeur initiale : {mon_rectangle.get_largeur()}")
print()
# Modifier la longueur et la largeur
mon_rectangle.set_longueur(10)
mon_rectangle.set_largeur(5)

# Afficher les valeurs modifiées
print()
print("Valeur Modifiée :")
print(f"Nouvelle longueur : {mon_rectangle.get_longueur()}")
print(f"Nouvelle largeur : {mon_rectangle.get_largeur()}")
print()