class Rectangle:
    
    def __init__(self, longueur , largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    # Assesseurs (getters)  
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur
    
    # Mutateurs (setters)    
    def set_longueur(self, longueur):
        self.__longueur = longueur
        
    def set_largeur(self, largeur):
        self.__largeur = largeur
        
# Création d'un rectangle
rect = Rectangle(10, 5)

# Affichage des valeurs initiales
print(f"Longueur initiale : {rect.get_longueur()}")
print(f"Largeur initiale : {rect.get_largeur()}")

# Modification des valeurs
rect.set_longueur(20)
rect.set_largeur(10)

# Vérification que les modifications ont été prises en compte
print(f"Nouvelle longueur : {rect.get_longueur()}")
print(f"Nouvelle largeur : {rect.get_largeur()}")