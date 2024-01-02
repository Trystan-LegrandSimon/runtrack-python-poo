#!/usr/local/bin/python3.12

class Operation:
    
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
    def addition(self):
        result = self.nombre1 + self.nombre2
        return result

# Instanciation de la classe
operation_instance = Operation(12, 3)

# Appel de la méthode addition
resultat_addition = operation_instance.addition()

# Impression du résultat en console
print(f"L'Operation est : {operation_instance.nombre1} + {operation_instance.nombre2}")
print(f"Résultat de l'addition : {resultat_addition}")