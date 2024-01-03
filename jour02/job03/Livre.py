class Livre:
    
    def __init__(self):
        self.__titre = input("Entrez le titre du livre : ")
        self.__auteur = input("Entrez le nom de l'auteur : ")
        self.set_pages(int(input("Entrez le nombre de pages : ")))
        self.__disponible = True  
        print(f"Le livre '{self.__titre}' a été créé.")
    
    # Assesseurs (getters)  
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur
    
    def get_pages(self):
        return self.__pages
    
    # Mutateurs (setters)    
    def set_titre(self, titre):
        self.__titre = titre
        print(f"Le titre du livre a été changé en '{self.__titre}'.")
        
    def set_auteur(self, auteur):
        self.__auteur = auteur
        print(f"L'auteur du livre a été changé en '{self.__auteur}'.")
        
    def set_pages(self, pages):
        if isinstance(pages, int) and pages > 0:
            self.__pages = pages
            print(f"Le nombre de pages du livre a été changé en {self.__pages}.")
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")
            
    # Méthodes pour gérer l'emprunt et le retour du livre
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():  # Vérifie si le livre est disponible
            self.__disponible = False
            print(f"Le livre '{self.__titre}' a été emprunté.")
        else:
            print("Erreur : Le livre n'est pas disponible.")
    
    def rendre(self):
        if not self.verification():  # Vérifie si le livre a été emprunté
            self.__disponible = True
            print(f"Le livre '{self.__titre}' a été rendu.")
        else:
            print("Erreur : Le livre n'a pas été emprunté.")

# Création d'un livre
livre = Livre()


            