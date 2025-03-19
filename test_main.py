class Voiture:
    """Classe représentant une voiture."""

    def __init__(self, marque: str, modele: str, vitesse: int =0) -> None:
        """Initialise une nouvelle voiture."""
        self.marque = marque
        self.modele = modele
        self.vitesse = vitesse

    def description(self):
        """Affiche les informations de la voiture."""
        return (f"{self.marque} {self.modele}, vitesse : {self.vitesse} km/h")

    def accelerer(self, vitesse: int):
        """Accélère la voiture."""
        self.vitesse += vitesse
        return (f"La voiture accélère de {self.vitesse} km/h, vitesse actuelle : {self.vitesse} km/h")


def add(a: int, b: int) -> int:
    """Retourne la somme de deux nombres."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Retourne la différence entre deux nombres."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Retourne le produit de deux nombres."""
    return a * b


def divide(a: int, b: int) -> float:
    """
    Retourne le quotient de deux nombres.
    Lève une exception en cas de division par zéro.
    """
    if b == 0:
        raise ValueError("Division par zéro non autorisée")
    return a / b


if __name__ == "__main__":
    print("Addition de 5 et 3:", add(5, 3))
    print("Soustraction de 10 et 4:", subtract(10, 4))
    print("Multiplication de 6 et 7:", multiply(6, 7))
    print("Division de 8 par 2:", divide(8, 2))

    ma_voiture = Voiture("Peugeot", "208")
    ta_voiture = Voiture("Renault", "Clio", vitesse=50)

    print(ma_voiture.description())
    ta_voiture.accelerer(20)
    print(ta_voiture.description())