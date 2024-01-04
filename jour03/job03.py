#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"Titre: {self.titre} - Description: {self.description} - Statut: {self.statut}"

class ListeDeTaches:
    
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)

    def supprimer_tache(self, tache):
        self.taches.remove(tache)

    def marquer_comme_finie(self, tache):
        tache.statut = "Terminée"

    def afficher_liste(self):
        for tache in self.taches:
            print(tache)

    def filter_liste(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]

# Tester le code
tache1 = Tache("Faire les courses", "Acheter des légumes")
tache2 = Tache("Réviser pour l'examen", "Chapitres 1 à 5")
tache3 = Tache("Faire du sport", "Jogging dans le parc")

liste_taches = ListeDeTaches()

liste_taches.ajouter_tache(tache1)
liste_taches.ajouter_tache(tache2)
liste_taches.ajouter_tache(tache3)

print("Liste initiale :")
liste_taches.afficher_liste()

print("\nTâches à faire :")
taches_a_faire = liste_taches.filter_liste("À faire")
for tache in taches_a_faire:
    print(tache)

# Supprimer une tâche
print("\nSupprimer la tâche 'Faire les courses' :")
liste_taches.supprimer_tache(tache1)
liste_taches.afficher_liste()

# Marquer une tâche comme terminée
print("\nMarquer la tâche 'Réviser pour l'examen' comme terminée :")
liste_taches.marquer_comme_finie(tache2)
liste_taches.afficher_liste()