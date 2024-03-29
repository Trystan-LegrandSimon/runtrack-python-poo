#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

'''
    Méthod Privée
'''

class Commande:
    
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  # Dictionnaire pour stocker les plats (nom, prix, statut)
        self.__statut_commande = "en cours"  # Statut par défaut

    def ajouter_plat(self, nom_plat, prix_plat):
        if self.__statut_commande == "en cours":
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "commandé"}
            print(f"Plat '{nom_plat}' ajouté à la commande.")
        else:
            print("Impossible d'ajouter un plat à une commande terminée ou annulée.")

    def annuler_commande(self):
        if self.__statut_commande == "en cours":
            self.__plats_commandes.clear()
            self.__statut_commande = "annulée"
            print("Commande annulée.")
        else:
            print("Impossible d'annuler une commande déjà terminée ou annulée.")

    def calculer_total(self):
        return sum(plat["prix"] for plat in self.__plats_commandes.values())

    def afficher_commande(self):
        print(f"Commande n°{self.__numero_commande} - Statut: {self.__statut_commande}")
        for nom_plat, plat_info in self.__plats_commandes.items():
            print(f"{nom_plat}: {plat_info['prix']} € - Statut: {plat_info['statut']}")
        total = self.calculer_total()
        print(f"Total à payer: {total} € (TVA incluse: {self.calculer_tva(total)} €)")

    def calculer_tva(self, montant):
        tva = montant * 0.2  # Exemple de TVA à 20%
        return round(tva, 2)  # Arrondi à deux décimales

# Exemple d'utilisation
commande1 = Commande(1)

commande1.ajouter_plat("Pizza", 15.99)
commande1.ajouter_plat("Salade", 8.50)

commande1.afficher_commande()

commande1.annuler_commande()

commande1.ajouter_plat("Burger", 12.50)
commande1.afficher_commande()