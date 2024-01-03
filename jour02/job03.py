#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

'''
    Méthod Privée
'''

class Livre:
    
    def __init__(self, titre, auteur, nombre_pages):
        self._titre = titre
        self._auteur = auteur
        self._nombre_pages = nombre_pages
        self._disponible = True

    # Assesseurs (getters)
    def get_titre(self):
        return self._titre

    def get_auteur(self):
        return self._auteur

    def get_nombre_pages(self):
        return self._nombre_pages

    def is_disponible(self):
        return self._disponible

    # Mutateurs (setters)
    def set_titre(self, titre):
        self._titre = titre

    def set_auteur(self, auteur):
        self._auteur = auteur

    def set_nombre_pages(self, nombre_pages):
        # Vérifier si le nouveau nombre de pages est un entier positif
        if isinstance(nombre_pages, int) and nombre_pages > 0:
            self._nombre_pages = nombre_pages
        else:
            print("⚠️ Erreur : Le nombre de pages doit être un entier positif.")

    # Méthode de vérification de disponibilité
    def verification(self):
        return self._disponible

    # Méthode d'emprunt
    def emprunter(self):
        if self._disponible:
            print("Le livre est disponible. Emprunt en cours.")
            self._disponible = False
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    # Méthode de rendu
    def rendre(self):
        if not self._disponible:
            print("Le livre a été rendu avec succès.")
            self._disponible = True
        else:
            print("Le livre est déjà disponible.")

# Exemple d'utilisation
mon_livre = Livre("Titre du Livre", "Auteur du Livre", 200)

# Afficher la disponibilité initiale
print(f"\nDisponible : {mon_livre.verification()}\n")

# Emprunter le livre
mon_livre.emprunter()

# Vérifier la disponibilité après l'emprunt
print(f"\nDisponible : {mon_livre.verification()}\n")

# Rendre le livre
mon_livre.rendre()

# Vérifier la disponibilité après le rendu
print(f"\nDisponible : {mon_livre.verification()}\n")