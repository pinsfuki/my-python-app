# main.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    print("3 + 5 =", add(3, 5))


import os # Erreur : import inutilisé
def add(a,b): # Avertissement : pas d'espace après la virgule
    return a+b # Avertissement : indentation incorrecte (doit être 4 espaces)
def multiply(x, y):
    return x * y # Avertissement : espace manquant avant le commentaire
class MyClass:
    def __init__(self):
        self.value= 0 # Avertissement : espace manquant autour de l'opérateur '='