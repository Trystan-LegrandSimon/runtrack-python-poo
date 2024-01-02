#!/usr/local/bin/python3.12

class Point:
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")
        
    def afficherX(self):
        print(f"Coordonnée x : {self.x}")
        
    def afficherY(self):
        print(f"Coordonnée y : {self.y}")
        
    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x
        
    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y

# Exemple d'utilisation de la classe Point
point_instance = Point(3, 4)

# Affichage des coordonnées initiales
point_instance.afficherLesPoints()

# Affichage des coordonnées x et y
point_instance.afficherX()
point_instance.afficherY()

# Changement des coordonnées x et y
point_instance.changerX(7)
point_instance.changerY(10)

# Affichage des nouvelles coordonnées
point_instance.afficherLesPoints()