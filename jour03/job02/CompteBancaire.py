class CompteBancaire:
    
    def __init__(self, numerocompte, nom, prenom, solde, decouvert=False):
        self.__numerocompte = numerocompte  
        self.__nom = nom  
        self.__prenom = prenom  
        self.__solde = solde  
        self.__decouvert = decouvert  # Autorisation de découvert (True si autorisé)

    def afficher(self):
        print(f"Le compte N°{self.__numerocompte} est au nom de {self.__nom} {self.__prenom}.")

    def afficherSolde(self):
        print(f"Le solde du compte N°{self.__numerocompte} est de {self.__solde} euros.")
        
    def versement(self, montant):
        self.__solde += montant  # Ajoute le montant au solde
        print(f"Versement de {montant} euros effectué. Nouveau solde : {self.__solde} euros.")
        
    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert:  # Vérifie si le solde est suffisant ou si le découvert est autorisé
            self.__solde -= montant  # Soustrait le montant du solde
            print(f"Retrait de {montant} euros effectué. Nouveau solde : {self.__solde} euros.")
        else:
            print("Solde insuffisant pour effectuer ce retrait.")
            
    def agios(self):
        if self.__solde < 0:  # Vérifie si le solde est négatif
            self.__solde *= 1.05  # Applique des agios de 5%
            print(f"Agios appliqués. Nouveau solde : {self.__solde} euros.")
            
    def virement(self, compte, montant):
        if self.__solde >= montant or self.__decouvert:  # Vérifie si le solde est suffisant ou si le découvert est autorisé
            self.__solde -= montant  # Soustrait le montant du solde
            compte.__solde += montant  # Ajoute le montant au solde du compte destinataire
            print(f"Un virement de {montant} euros a été effectué vers le compte N°{compte.__numerocompte}.")
        else:
            print("Solde insuffisant pour effectuer ce virement.")

# Création de deux instances de la classe CompteBancaire
compte1 = CompteBancaire('934', 'Harry', 'Potter', 2000)  # Compte avec solde positif
compte2 = CompteBancaire('935', 'Hermione', 'Granger', -500, True)  # Compte avec solde négatif et découvert autorisé

# Effectue un virement du compte1 vers le compte2
compte1.virement(compte2, 500)

compte1.afficherSolde()
compte2.afficherSolde()
     