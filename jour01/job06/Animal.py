class Animal:
    
    def __init__(self):
        self.age = 0
        self.prenom = "" 
        
    def set_age(self, age):
        self.age = age
        
    def set_prenom(self, prenom):
        self.prenom = prenom
        
    def vieillir(self):
        print(f"L'âge de l'animal {self.age} ans")
        self.age += 1
        print(f"L'âge de l'animal {self.age} ans")
        
    def nommer(self, prenom):
        self.prenom = prenom
        print(f"L'animal se nomme {self.prenom}")
        
        
caracteristique = Animal()
caracteristique.vieillir()
caracteristique.nommer("Luna")


