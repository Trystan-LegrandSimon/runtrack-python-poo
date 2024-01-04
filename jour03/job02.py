#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

class CompteBancaire:
    
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"\nNuméro de compte: {self.__numero_compte}")
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Solde: {self.__solde} EUR\n")
        print("-" * 20 + "\n")

    def afficher_solde(self):
        print(f"Solde actuel: {self.__solde} EUR\n")
        print("-" * 20 + "\n")
        
    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} EUR effectué.")
        self.afficher_solde()

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} EUR effectué.")
            self.afficher_solde()
        else:
            print("Opération impossible. Solde insuffisant.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux_agios
            self.__solde -= agios
            print(f"Des agios de {agios} EUR ont été appliqués.")
            self.afficher_solde()

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} EUR effectué vers le compte {compte_destinataire.__numero_compte}.")
            self.afficher_solde()
        else:
            print("Opération impossible. Solde insuffisant.")

# Créer une instance de la classe CompteBancaire
compte1 = CompteBancaire(numero_compte="12345", nom="Dupont", prenom="Jean", solde=1000)

# Afficher les détails du compte
compte1.afficher()

# Faire un versement
compte1.versement(500)

# Faire un retrait
compte1.retrait(200)

# Ajouter l'attribut decouvert à True
compte2 = CompteBancaire(numero_compte="67890", nom="Durand", prenom="Alice", solde=-500, decouvert=True)

# Faire un versement du compte1 vers le compte2 pour remettre le compte2 à zéro
compte1.virement(compte2, 500)