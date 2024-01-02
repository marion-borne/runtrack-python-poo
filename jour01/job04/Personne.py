class Personne:
    
    def __init__(self, nom , prenom):
        self.nom = nom
        self.prenom = prenom
        
    def set_nom(self, nom):
        self.nom = nom
        
    def set_prenom(self, prenom):
        self.prenom = prenom
        
    def SePresenter(self):
        return f"Je suis {self.nom} {self.prenom}"
        
        
identite1 = Personne("John", "Doe")
identite2 = Personne("Jean", "Dupond")
print(identite1.SePresenter())
print(identite2.SePresenter())