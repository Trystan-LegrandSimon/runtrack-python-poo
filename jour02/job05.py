#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

'''
    Méthod Privée
'''

class Voiture:
    
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    # Assesseurs (getters)
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    # Mutateurs (setters)
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    # Méthode de démarrage
    def demarrer(self):
        if self.verifier_plein():
            print("La voiture démarre.")
            self.__en_marche = True
        else:
            print("La voiture ne peut pas démarrer. Le réservoir est trop bas...")

    # Méthode d'arrêt
    def arreter(self):
        print("La voiture s'arrête.")
        self.__en_marche = False

    # Méthode privée pour vérifier le niveau du réservoir
    def verifier_plein(self):
        return self.__reservoir > 5

# Exemple d'utilisation
ma_voiture = Voiture("CUPRA", "Ateca", 2019, 60000)

# Affichage des informations initiales
print(f"Marque: {ma_voiture.get_marque()}")
print(f"Modèle: {ma_voiture.get_modele()}")
print(f"Année: {ma_voiture.get_annee()}")
print(f"Kilométrage: {ma_voiture.get_kilometrage()} kms")
print(f"En marche: {ma_voiture.get_en_marche()}")
print("-" * 50)

# Démarrage de la voiture
ma_voiture.demarrer()

# Affichage après le démarrage
print(f"En marche: {ma_voiture.get_en_marche()}")

# Arrêt de la voiture
ma_voiture.arreter()

# Affichage après l'arrêt
print(f"En marche: {ma_voiture.get_en_marche()}")