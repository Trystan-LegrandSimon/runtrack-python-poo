#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

class Joueur:
    
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquer_un_but(self):
        self.buts_marques += 1

    def effectuer_une_passe_decisive(self):
        self.passes_decisives += 1

    def recevoir_un_carton_jaune(self):
        self.cartons_jaunes += 1

    def recevoir_un_carton_rouge(self):
        self.cartons_rouges += 1

    def afficher_statistiques(self):
        print(f"Statistiques de {self.nom} (Numéro {self.numero}, Position: {self.position}):")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives effectuées: {self.passes_decisives}")
        print(f"Cartons jaunes reçus: {self.cartons_jaunes}")
        print(f"Cartons rouges reçus: {self.cartons_rouges}")
        print("\n")


class Equipe:
    
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def afficher_statistiques_joueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom} :")
        for joueur in self.joueurs:
            joueur.afficher_statistiques()

    def mettre_a_jour_statistiques_joueur(self, numero_joueur, action):
        for joueur in self.joueurs:
            if joueur.numero == numero_joueur:
                if action == "but":
                    joueur.marquer_un_but()
                elif action == "passe_decisive":
                    joueur.effectuer_une_passe_decisive()
                elif action == "carton_jaune":
                    joueur.recevoir_un_carton_jaune()
                elif action == "carton_rouge":
                    joueur.recevoir_un_carton_rouge()
                else:
                    print("Action non reconnue.")
                break


# Créer plusieurs joueurs
joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Modric", 8, "Milieu de terrain")

# Créer deux équipes
equipe1 = Equipe("Équipe A")
equipe2 = Equipe("Équipe B")

# Ajouter les joueurs aux équipes
equipe1.ajouter_joueur(joueur1)
equipe1.ajouter_joueur(joueur2)

equipe2.ajouter_joueur(joueur3)

# Afficher les statistiques initiales
print("Statistiques initiales :")
equipe1.afficher_statistiques_joueurs()
equipe2.afficher_statistiques_joueurs()

# Simuler un match
print("Simuler un match :")
equipe1.mettre_a_jour_statistiques_joueur(10, "but")  # Messi marque un but
equipe1.mettre_a_jour_statistiques_joueur(7, "carton_jaune")  # Ronaldo reçoit un carton jaune
equipe2.mettre_a_jour_statistiques_joueur(8, "passe_decisive")  # Modric effectue une passe décisive
equipe2.mettre_a_jour_statistiques_joueur(8, "carton_rouge")  # Modric reçoit un carton rouge

# Afficher les statistiques après le match
print("Statistiques après le match :")
equipe1.afficher_statistiques_joueurs()
equipe2.afficher_statistiques_joueurs()