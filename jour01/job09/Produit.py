class Produit:
    
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
        
    def afficher(self):
        return f"Les informations du produit {self.nom} sont :\nLe prix HT est {self.prixHT}\nLa TVA est de {self.TVA}\nLe prix TTC est {self.CalculerPrixTTC()}"
        
    def CalculerPrixTTC(self):
        result = self.prixHT + (self.prixHT * self.TVA / 100)
        return result
    
    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom
        
    def modifier_prixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT
    
    def get_nom(self):
        return self.nom
    
    def get_prixHT(self):
        return self.prixHT
        
    def get_TVA(self):
        return self.TVA
        
#Création des produits
prod1 = Produit("Tomate", 2, 15) # 15% de TVA
prod2 = Produit("Gruyère", 5, 15) # 15% de TVA

# Modification du nom et du prix des produits
prod1.modifier_nom("Tomate cerise")
prod1.modifier_prixHT(2.5)
prod2.modifier_nom("Gruyère râpé")
prod2.modifier_prixHT(5.5)

# Affichage des informations pour chaque produit
for Produit in [prod1, prod2]:
    print(Produit.afficher())