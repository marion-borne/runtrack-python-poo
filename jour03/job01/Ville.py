class Ville:
    
    def __init__(self, nom, nbr_habitants):
        self.__nom = nom
        self.__nbrhabitants = nbr_habitants

    def ajouterPopulation(self):
        self.__nbrhabitants += 1 # Augmente le nombre d'habitants de 1

    def getPopulation(self):
        return self.__nbrhabitants # Retourne le nombre d'habitants de la ville

class Personne:
    
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.__ville.ajouterPopulation() # Appelle la méthode ajouterPopulation de la ville de résidence

# Création des objets Ville
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Affichage du nombre d'habitants avant ajout des nouvelles personnes
print(f"Population de Paris : {paris.getPopulation()} habitants")
print(f"Population de Marseille : {marseille.getPopulation()} habitants")

# Création des objets Personne
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Affichage du nombre d'habitants après l'arrivée des nouvelles personnes
print(f"Mise à jour de la population de Paris : {paris.getPopulation()} habitants")
print(f"Mise à jour de la population de Marseille : {marseille.getPopulation()} habitants")

        
    
        
    
    