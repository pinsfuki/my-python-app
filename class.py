class Vehicule:
    """Classe abstraite representant un vehicule."""

    def __init__(self, marque: str, modele: str, type_energie: str, vitesse: int = 0) -> None:
        """
        Initialise un vehicule.

        :param marque: La marque du vehicule.
        :param modele: Le modele du vehicule.
        :param type_energie: Le type d'energie (Thermique ou Electrique).
        :param vitesse: La vitesse initiale du vehicule (par defaut 0).
        """
        self.marque = marque
        self.modele = modele
        self.type_energie = type_energie
        self.vitesse = vitesse

    def demarrer(self) -> None:
        """Demarre le vehicule."""
        print(f"{self.marque} {self.modele} ({self.type_energie}) demarre.")

    def accelerer(self) -> None:
        """Accele le vehicule en augmentant sa vitesse."""
        self.vitesse += 10
        print(f"{self.marque} {self.modele} accelere a {self.vitesse} km/h.")

    def arreter(self) -> None:
        """Arrete le vehicule."""
        self.vitesse = 0
        print(f"{self.marque} {self.modele} s'arrete.")

    def __str__(self) -> str:
        """Represente sous forme de chaine le vehicule."""
        return f"{self.marque} {self.modele} ({self.type_energie})"


class Voiture(Vehicule):
    """Classe representant une voiture, heritee de la classe Vehicule."""

    def __init__(self, marque: str, modele: str, type_energie: str, vitesse: int = 0) -> None:
        """
        Initialise une voiture.

        :param marque: La marque de la voiture.
        :param modele: Le modele de la voiture.
        :param type_energie: Le type d'energie de la voiture (Thermique ou Electrique).
        :param vitesse: La vitesse initiale de la voiture (par defaut 0).
        """
        super().__init__(marque, modele, type_energie, vitesse)

    def klaxonner(self) -> None:
        """Fait klaxonner la voiture."""
        print(f"{self.marque} {self.modele} klaxonne.")


class Scooter(Vehicule):
    """Classe representant un scooter, heritee de la classe Vehicule."""
    
    def __init__(self, marque: str, modele: str, type_energie: str, vitesse: int = 0) -> None:
        """
        Initialise un scooter.

        :param marque: La marque du scooter.
        :param modele: Le modele du scooter.
        :param type_energie: Le type d'energie du scooter (Thermique ou Electrique).
        :param vitesse: La vitesse initiale du scooter (par defaut 0).
        """
        super().__init__(marque, modele, type_energie, vitesse)

    def faire_un_wheelie(self) -> None:
        """Fait un wheelie avec le scooter."""
        print(f"{self.marque} {self.modele} fait un wheelie.")


# Exemple d'utilisation avec des objets :

def test_vehicules():
    """Fonction pour tester les vehicules."""
    # Creation de vehicules
    voiture_thermique = Voiture("Toyota", "Corolla", "Thermique")
    voiture_electrique = Voiture("Tesla", "Model 3", "Electrique")
    scooter_thermique = Scooter("Honda", "PCX", "Thermique")
    scooter_electrique = Scooter("NIU", "MQi GT", "Electrique")

    # Affichage des vehicules
    print(voiture_thermique)
    print(voiture_electrique)
    print(scooter_thermique)
    print(scooter_electrique)

    # Demarrage des vehicules
    print("\nDemarrage des vehicules :")
    voiture_thermique.demarrer()
    voiture_electrique.demarrer()
    scooter_thermique.demarrer()
    scooter_electrique.demarrer()

    # Acceleration
    print("\nAcceleration des vehicules :")
    voiture_thermique.accelerer()
    scooter_thermique.accelerer()

    # Actions specifiques
    print("\nActions specifiques :")
    voiture_thermique.klaxonner()
    scooter_thermique.faire_un_wheelie()

# Test des vehicules
test_vehicules()
