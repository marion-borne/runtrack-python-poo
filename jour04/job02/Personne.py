class Personne:
    def __init__(self, age):
        self.age = age

    def bonjour(self):
        return "Bonjour!"

class Eleve(Personne):
    def allerEnCours(self):
        return "Eleve, je vais en cours."

class Professeur(Personne):
    def enseigner(self):
        return "Professeur, je commence le cours."

# Création d'un objet Eleve
eleve = Eleve(15)
print(eleve.bonjour())  # Affiche "Bonjour!"
print(eleve.allerEnCours())  # Affiche "Je vais en cours."

# Création d'un objet Professeur
professeur = Professeur(40)
print(professeur.bonjour())  # Affiche "Bonjour!"
print(professeur.enseigner())  # Affiche "Commençons le cours."
