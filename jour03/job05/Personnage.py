class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        adversaire.seFaireAttaquer(30)
        print(f"{self.nom} attaque {adversaire.nom}. {adversaire.nom} a maintenant {adversaire.vie} points de vie.")

    def seFaireAttaquer(self, degats):
        self.vie -= degats
        print(f"{self.nom} a été attaqué et a perdu {degats} points de vie.")
        self.verifierSante()

    def verifierSante(self):
        if self.vie <= 0:
            print(f"{self.nom} est battu!")
            return False
        return True

class Jeu:
    def __init__(self):
        self.niveau = None
        self.joueur = None
        self.ennemi = None

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2, 3): "))
        if self.niveau == 1:
            vie = 50
        elif self.niveau == 2:
            vie = 100
        else:
            vie = 150
        return vie

    def lancerJeu(self):
        vie = self.choisirNiveau()
        self.joueur = Personnage("Marion", vie)
        self.ennemi = Personnage("Idriss", vie)
        while self.joueur.verifierSante() and self.ennemi.verifierSante():
            self.joueur.attaquer(self.ennemi)
            if not self.ennemi.verifierSante():
                break
            self.ennemi.attaquer(self.joueur)
        self.verifierGagnant()

    def verifierGagnant(self):
        if self.joueur.vie <= 0:
            print("L'ennemi a gagné!")
        else:
            print("Le joueur a gagné!")

jeu = Jeu()
jeu.lancerJeu()



