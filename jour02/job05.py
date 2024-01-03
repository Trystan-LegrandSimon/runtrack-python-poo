#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

'''
    Méthod Privée
'''

class Voiture:
    
    def __init__(self, marque, modele, annee, kilometrage):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = False
        self._reservoir = 50

    # Assesseurs (getters)
    def get_marque(self):
        return self._marque

    def get_modele(self):
        return self._modele

    def get_annee(self):
        return self._annee

    def get_kilometrage(self):
        return self._kilometrage

    def get_en_marche(self):
        return self._en_marche

    # Mutateurs (setters)
    def set_marque(self, marque):
        self._marque = marque

    def set_modele(self, modele):
        self._modele = modele

    def set_annee(self, annee):
        self._annee = annee

    def set_kilometrage(self, kilometrage):
        self._kilometrage = kilometrage

    # Méthode de démarrage
    def demarrer(self):
        if self._verifier_plein():
            print("La voiture démarre.")
            self._en_marche = True
        else:
            print("La voiture ne peut pas démarrer. Le réservoir est trop bas...")

    # Méthode d'arrêt
    def arreter(self):
        print("La voiture s'arrête.")
        self._en_marche = False

    # Méthode privée pour vérifier le niveau du réservoir
    def _verifier_plein(self):
        return self._reservoir > 5

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