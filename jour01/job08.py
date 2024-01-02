#!/usr/local/bin/python3.12

import math

class Cercle:
    
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Rayon du cercle : {self.rayon}")

    def circonférence(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon**2

    def diametre(self):
        return 2 * self.rayon

# Création de deux cercles avec des rayons 4 et 7
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Affichage des informations, circonférence, diamètre et aire pour chaque cercle
for cercle in [cercle1, cercle2]:
    print()
    cercle.afficherInfos()
    print(f"Circonférence : {cercle.circonférence()}")
    print(f"Diamètre : {cercle.diametre()}")
    print(f"Aire : {cercle.aire()}")
    print()