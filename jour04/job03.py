#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

class Rectangle:
    
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    @property
    def longueur(self):
        return self.__longueur

    @property
    def largeur(self):
        return self.__largeur

    @longueur.setter
    def longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    @largeur.setter
    def largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

    def __calculer_perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def __calculer_surface(self):
        return self.__longueur * self.__largeur

    def afficher_perimetre_surface(self):
        perimetre = self.__calculer_perimetre()
        surface = self.__calculer_surface()
        print(f"Périmètre du rectangle : {perimetre} cm")
        print(f"Surface du rectangle : {surface} cm²")


class Parallelepipede(Rectangle):
    
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    @property
    def hauteur(self):
        return self.__hauteur

    @hauteur.setter
    def hauteur(self, nouvelle_hauteur):
        self.__hauteur = nouvelle_hauteur

    def afficher_volume(self):
        volume = self._Rectangle__longueur * self._Rectangle__largeur * self.__hauteur
        print(f"Volume du parallélépipède : {volume} m³")


# Instanciation de la classe Rectangle
rectangle1 = Rectangle(longueur = 5, largeur = 3)
rectangle1.afficher_perimetre_surface()

# Modification des attributs avec les mutateurs
rectangle1.longueur = 8
rectangle1.largeur = 4
rectangle1.afficher_perimetre_surface()

# Instanciation de la classe Parallelepipede
parallelepiped1 = Parallelepipede(longueur = 5, largeur = 3, hauteur = 2)
parallelepiped1.afficher_volume()