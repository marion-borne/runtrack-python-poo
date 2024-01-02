import math

class Cercle:
    
    def __init__(self, nom, rayon):
        self.nom = nom
        self.rayon = rayon
        
    def changerRayon(self, rayon):
        self.rayon = rayon
        print(f'La nouvelle valeur du rayon est {self.rayon}')
        
    def afficherInfos(self):
        print(f"Les informations du {self.nom} sont :")
        print(f"Le Rayon est de {self.rayon}")
        print(f"La Circonférence est de {self.circonference()}")
        print(f"L'aire est de {self.aire()}")
        print(f"Le diametre est de {self.diametre()}")
        
    def circonference(self):
        result = 2 * math.pi * self.rayon
        return result
        
    def aire(self):
        result = math.pi * (self.rayon ** 2)
        return result
        
    def diametre(self):
        result = 2 * self.rayon 
        return result
        
#Création des cercles
cercle1 = Cercle("Cercle 1", 4)
cercle2 = Cercle("Cercle 2", 7)

# Affichage des informations pour chaque cercle
for cercle in [cercle1, cercle2]:
    cercle.afficherInfos()
