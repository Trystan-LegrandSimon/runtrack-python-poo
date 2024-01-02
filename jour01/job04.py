#!/usr/local/bin/python3.12

class Personne:
    
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
    def SePresenter(self):
        return f"Je m'appelle {self.prenom} {self.nom}"

# Instanciation de plusieurs personnes
personne1 = Personne("Doe", "John")
personne2 = Personne("Smith", "Jane")
personne3 = Personne("Dupont", "Pierre")

# Appel de la méthode SePresenter pour chaque personne
presentation1 = personne1.SePresenter()
presentation2 = personne2.SePresenter()
presentation3 = personne3.SePresenter()

# Impression des présentations
print(presentation1)
print(presentation2)
print(presentation3)