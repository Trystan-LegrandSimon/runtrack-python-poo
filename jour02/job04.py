#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

'''
    Méthod Privée
'''

class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self._nom = nom
        self._prenom = prenom
        self._numero_etudiant = numero_etudiant
        self._credits = 0
        self._level = self._student_eval()

    def _student_eval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def add_credits(self, credits):
        if credits > 0:
            self._credits += credits
            self._level = self._student_eval()
            print(f"\nLe nomre de crédits de {self._nom} {self._prenom} est de : {self._credits}\n")
        else:
            print("⚠️ Erreur : Le nombre de crédits ajouté doit être supérieur à zéro.")

    def student_info(self):
        print(f"Informations de l'étudiant:")
        print(f"Nom: {self._nom}")
        print(f"Prénom: {self._prenom}")
        print(f"Id: {self._numero_etudiant}")
        print(f"Niveau: {self._level}")
        print("--------------------------------------------------")

# Instanciation de l'objet représentant l'étudiant John Doe
john_doe = Student("John", "Doe", 145)

'''
    Ajout de crédits à trois reprises et 
    Affichage des informations de l'étudiant
'''

john_doe.add_credits(30)
john_doe.student_info()

john_doe.add_credits(40)
john_doe.student_info()

john_doe.add_credits(25)
john_doe.student_info()