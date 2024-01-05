class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

# Création d'un objet Rectangle
rectangle = Rectangle(2024, 200)

# Affichage de l'aire du rectangle avec une phrase
print(f"L'aire du rectangle est {rectangle.aire()}.")

