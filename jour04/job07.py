#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

import random

class Carte:
    
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu(Carte):
    
    def __init__(self):
        super().__init__(0, "")
        self.paquet = self.initialiser_paquet()

    def initialiser_paquet(self):
        valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1]
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(paquet)
        return paquet

    def tirer_carte(self):
        return self.paquet.pop(0)

    def calculer_total(self, main):
        total = sum(carte.valeur for carte in main)
        
        for carte in main:
            if carte.valeur == 1 and total + 10 <= 21:
                total += 10
        return total

def afficher_main(main, nom):
    print(f"\nMain de {nom}:")
    
    for carte in main:
        print(f"{carte.valeur} de {carte.couleur}")
    print(f"Total : {jeu.calculer_total(main)}")

def determiner_resultat(main_joueur, main_croupier):
    total_joueur = jeu.calculer_total(main_joueur)
    total_croupier = jeu.calculer_total(main_croupier)

    if total_joueur > 21:
        return "Le Joueur a dépassé 21. Le croupier gagne.\n"
    elif total_croupier > 21:
        return "Le Croupier a dépassé 21. Le joueur gagne.\n"
    elif total_joueur > total_croupier:
        return "Le Joueur gagne.\n"
    elif total_joueur < total_croupier:
        return "Le Croupier gagne.\n"
    else:
        return "Égalité. Personne ne gagne.\n"

if __name__ == "__main__":
    jeu = Jeu()

    main_joueur = [jeu.tirer_carte(), jeu.tirer_carte()]
    main_croupier = [jeu.tirer_carte(), jeu.tirer_carte()]

    afficher_main(main_joueur, "Joueur")
    afficher_main(main_croupier, "Croupier")

    try:
        while input("Voulez-vous prendre une carte ? (Oui/Non): ").lower() == "oui":
            main_joueur.append(jeu.tirer_carte())
            afficher_main(main_joueur, "joueur")
            if jeu.calculer_total(main_joueur) > 21:
                print("Le joueur a dépassé 21. Le croupier gagne.\n")
                exit()

    except KeyboardInterrupt:
        print("\n\nPartie interrompue. Au revoir !\n")
        exit()

    while jeu.calculer_total(main_croupier) < 17:
        main_croupier.append(jeu.tirer_carte())

    afficher_main(main_joueur, "joueur")
    afficher_main(main_croupier, "croupier")

    resultat = determiner_resultat(main_joueur, main_croupier)
    print(resultat)