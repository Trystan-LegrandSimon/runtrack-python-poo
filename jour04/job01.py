#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

class Personne:
    
    def __init__(self, age = 14):
        self.age = age

    def afficherAge(self):
        print(f"Âge de la personne : {self.age} an(s)")

    def bonjour(self):
        print("Hello")

    def modifierAge(self):
        
        try:
            nouvel_age = int(input("Entrez le nouvel âge de la personne : "))
            self.age = nouvel_age
        except ValueError:
            print("\n\nOpération annulée. Mauvaise saisie.\n")
        except KeyboardInterrupt:
            print("\n\nOpération annulée. Programme interrompu par l'utilisateur.\n")
        
class Eleve(Personne):
    
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    
    def __init__(self, matiereEnseignee, age):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

# Instanciation d'une personne et d'un élève
personne1 = Personne()
eleve1 = Eleve()

# Affichage de l'âge par défaut de l'élève
eleve1.afficherAge()

# Test de la méthode modifierAge pour la personne
personne1.afficherAge()
personne1.bonjour()
personne1.modifierAge()

# Affichage de l'âge mis à jour
personne1.afficherAge()