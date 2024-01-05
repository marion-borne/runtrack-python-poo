class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        adversaire.vie -= 10
        print(f"{self.nom} attaque {adversaire.nom}. {adversaire.nom} a maintenant {adversaire.vie} points de vie.")

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
        self.joueur = Personnage("Joueur", vie)
        self.ennemi = Personnage("Ennemi", vie)
        while self.joueur.vie > 0 and self.ennemi.vie > 0:
            self.joueur.attaquer(self.ennemi)
            if self.ennemi.vie <= 0:
                print("Le joueur a gagné!")
                break
            self.ennemi.attaquer(self.joueur)
            if self.joueur.vie <= 0:
                print("L'ennemi a gagné!")
                break

jeu = Jeu()
jeu.lancerJeu()
