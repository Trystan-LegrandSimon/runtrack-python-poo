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

    # Assesseurs (getters)
    def get_titre(self):
        return self._titre

    def get_auteur(self):
        return self._auteur

    def get_nombre_pages(self):
        return self._nombre_pages

    # Mutateurs (setters)
    def set_titre(self, nouveau_titre):
        self._titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self._auteur = nouvel_auteur

    def set_nombre_pages(self, nouveau_nombre_pages):
        # Vérifier si le nouveau nombre de pages est un entier positif
        if isinstance(nouveau_nombre_pages, int) and nouveau_nombre_pages > 0:
            self._nombre_pages = nouveau_nombre_pages
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