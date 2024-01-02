#!/usr/local/bin/python3.12

class Animal:
    
    def __init__(self, age=0, prenom=""):
        self.age = age
        self.prenom = prenom

    def vieillir(self):
        self.age += 1

    def nommer(self, nouveau_nom):
        self.prenom = nouveau_nom

# Instanciation de la classe
instance_animal = Animal()

# Utilisation des méthodes
instance_animal.vieillir()
instance_animal.nommer("Fido")

# Impression de l'âge et du nom de l'animal
print(f"L'âge de l'animal est : {instance_animal.age}")
print(f"Le nom de l'animal est : {instance_animal.prenom}")