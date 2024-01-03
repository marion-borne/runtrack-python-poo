class Voiture:
    
    def __init__(self, marque, modele, annee, kilometrage, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = reservoir

    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
        else:
            print("Le réservoir est vide. Veuillez le remplir sinon ca va être la panne !")

    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        return self.__reservoir


if __name__ == "__main__":
    ma_voiture = Voiture("Wolkswagen", "T-Roc", 2021, 32000)

    while True:
        print("\n1. Démarrer la voiture")
        print("2. Arrêter la voiture")
        print("3. Afficher les détails de la voiture")
        print("4. Quitter")
        choix = input("Choisissez une option : ")

        if choix == '1':
            ma_voiture.demarrer()
            if ma_voiture.get_en_marche():
                print("La voiture a démarré.")
            else:
                print("La voiture n'a pas pu démarrer. Le réservoir est vide, dommage :(")
        elif choix == '2':
            ma_voiture.arreter()
            print("La voiture est arrêtée.")
        elif choix == '3':
            print(f"Marque : {ma_voiture.get_marque()}")
            print(f"Modèle : {ma_voiture.get_modele()}")
            print(f"Année : {ma_voiture.get_annee()}")
            print(f"Kilométrage : {ma_voiture.get_kilometrage()}")
            print(f"En marche : {ma_voiture.get_en_marche()}")
            print(f"Réservoir : {ma_voiture.get_reservoir()}")
        elif choix == '4':
            break
        else:
            print("Option invalide. Veuillez réessayer.")

