#!/usr/bin/env python3.12
# -*- coding: utf-8 -*-

'''
    Méthode Privée
'''

class Student:

    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__level = self.student_eval()

    def student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.student_eval()
            print(f"\nLe nombre de crédits de {self.__nom} {self.__prenom} est de : {self.__credits}\n")  # Corrections ici
        else:
            print("⚠️ Erreur : Le nombre de crédits ajouté doit être supérieur à zéro.")

    def student_info(self):
        print(f"Informations de l'étudiant:")
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Id: {self.__numero_etudiant}")
        print(f"Niveau: {self.__level}")
        print("-" * 50)

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