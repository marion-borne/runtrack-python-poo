class Joueur:
    def __init__(self, nom, numero, position, buts=0, passes=0, cartons_jaunes=0, cartons_rouges=0):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = buts
        self.passes = passes
        self.cartons_jaunes = cartons_jaunes
        self.cartons_rouges = cartons_rouges

    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        return f'Nom: {self.nom}, Numéro: {self.numero}, Position: {self.position}, Buts: {self.buts}, Passes: {self.passes}, Cartons Jaunes: {self.cartons_jaunes}, Cartons Rouges: {self.cartons_rouges}'

class Equipe:
    def __init__(self, nom, joueurs=[]):
        self.nom = nom
        self.joueurs = joueurs

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        for joueur in self.joueurs:
            print(joueur.afficherStatistiques())

    def mettreAJourStatistiquesJoueur(self, nom, buts=None, passes=None, cartons_jaunes=None, cartons_rouges=None):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                if buts is not None:
                    joueur.buts = buts
                if passes is not None:
                    joueur.passes = passes
                if cartons_jaunes is not None:
                    joueur.cartons_jaunes = cartons_jaunes
                if cartons_rouges is not None:
                    joueur.cartons_rouges = cartons_rouges

def afficher_menu():
    print("1. Ajouter un joueur")
    print("2. Marquer un but")
    print("3. Effectuer une passe décisive")
    print("4. Recevoir un carton jaune")
    print("5. Recevoir un carton rouge")
    print("6. Afficher les statistiques des joueurs")
    print("7. Quitter le jeu")

equipe = Equipe('Equipe1')

while True:
    afficher_menu()
    choix = input("Entrez votre choix : ")
    if choix == '1':
        nom = input("Entrez le nom du joueur : ")
        numero = int(input("Entrez le numéro du joueur : "))
        position = input("Entrez la position du joueur : ")
        joueur = Joueur(nom, numero, position)
        equipe.ajouterJoueur(joueur)
    elif choix == '2':
        nom = input("Entrez le nom du joueur qui a marqué un but : ")
        equipe.mettreAJourStatistiquesJoueur(nom, buts=1)
    elif choix == '3':
        nom = input("Entrez le nom du joueur qui a effectué une passe décisive : ")
        equipe.mettreAJourStatistiquesJoueur(nom, passes=1)
    elif choix == '4':
        nom = input("Entrez le nom du joueur qui a reçu un carton jaune : ")
        equipe.mettreAJourStatistiquesJoueur(nom, cartons_jaunes=1)
    elif choix == '5':
        nom = input("Entrez le nom du joueur qui a reçu un carton rouge : ")
        equipe.mettreAJourStatistiquesJoueur(nom, cartons_rouges=1)
    elif choix == '6':
        equipe.afficherStatistiquesJoueurs()
    elif choix == '7':
        break

joueur1 = Joueur('Idriss', 1, 'Attaquant')
joueur2 = Joueur('Marion', 2, 'Défenseur')

equipe = Equipe('Equipe1')
equipe.ajouterJoueur(joueur1)
equipe.ajouterJoueur(joueur2)

joueur1.marquerUnBut()
