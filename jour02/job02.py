#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

'''
    Méthod Privée
'''

class Livre:
    
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages

    # Assesseurs (getters)
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_pages(self):
        return self.__nombre_pages

    # Mutateurs (setters)
    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_pages(self, nombre_pages):
        # Vérifier si le nouveau nombre de pages est un entier positif
        if isinstance(nombre_pages, int) and nombre_pages > 0:
            self.__nombre_pages = nombre_pages
        else:
            print("⚠️  Erreur : Le nombre de pages doit être un entier positif.")

# Exemple d'utilisation
mon_livre = Livre("Titre du Livre", "Auteur du Livre", 200)

# Afficher les valeurs initiales
print()
print(f"Titre : {mon_livre.get_titre()}")
print(f"Auteur : {mon_livre.get_auteur()}")
print(f"Nombre de pages : {mon_livre.get_nombre_pages()}")
print()

# Modifier le titre, l'auteur et le nombre de pages
mon_livre.set_titre("Nouveau Titre")
mon_livre.set_auteur("Nouvel Auteur")
mon_livre.set_nombre_pages(300)

# Afficher les valeurs modifiées
print()
print(f"Nouveau Titre : {mon_livre.get_titre()}")
print(f"Nouvel Auteur : {mon_livre.get_auteur()}")
print(f"Nouveau Nombre de pages : {mon_livre.get_nombre_pages()}")
print()

# Tentative de changer le nombre de pages avec une valeur invalide
mon_livre.set_nombre_pages(-50)