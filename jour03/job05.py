#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

import random

class Personnage:
    
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
        adversaire.vie -= degats

class Jeu:
    
    def __init__(self):
        self.niveau = 1

    def choisir_niveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2 ou 3) : "))

    def lancer_jeu(self):
        print("Bienvenue dans le jeu de combat!")
        self.choisir_niveau()

        joueur = Personnage("Joueur", self.niveau * 10)
        ennemi = Personnage("Ennemi", self.niveau * 10)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            ennemi.attaquer(joueur)

            self.afficher_etat_partie(joueur, ennemi)

        self.afficher_resultat(joueur, ennemi)

    def afficher_etat_partie(self, joueur, ennemi):
        print(f"\n{Jeu.separator()} État actuel de la partie {Jeu.separator()}")
        print(f"{joueur.nom} - Vie: {joueur.vie}")
        print(f"{ennemi.nom} - Vie: {ennemi.vie}")
        print(Jeu.separator())

    def afficher_resultat(self, joueur, ennemi):
        if joueur.vie <= 0:
            print("Vous avez perdu. L'ennemi a gagné.")
        else:
            print("Félicitations! Vous avez vaincu l'ennemi.")

    @staticmethod
    def separator():
        return "-" * 30


# Exécution du jeu
jeu = Jeu()
jeu.lancer_jeu()