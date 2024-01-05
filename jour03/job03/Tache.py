class Tache:
    def __init__(self, titre, description):
        self.titre = titre  
        self.description = description  
        self.statut = 'à faire'  # Au début, la tâche est toujours 'à faire'

class ListeDeTaches:
    # Quand on crée une liste de tâches, la liste est vide
    def __init__(self):
        self.taches = []  # On a une liste vide de tâches

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.statut = 'TERMINE'

    def afficherListe(self):
        return self.taches

    # On peut obtenir une liste de tâches qui ont un certain statut
    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]

# Création de plusieurs instances de Tache
tache1 = Tache('Aller chez le fromager', 'Acheter du Brie')
tache2 = Tache('Faire la valise pour les vacances', 'Etre à jour des machines')
tache3 = Tache('Sortir de chien', 'Lui essuyer le museau')

# Création d'une instance de ListeDeTaches et ajout des tâches
liste = ListeDeTaches()
liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

print("Toutes les tâches :")
for tache in liste.afficherListe():
    print(tache.titre, "-", tache.description, "-", tache.statut)

# Suppression d'une tâche
liste.supprimerTache(tache2)

# Changement du statut d'une tâche
liste.marquerCommeFinie(tache1)

# Affichage de toutes les tâches
print("Toutes les tâches après suppression et changement de statut :")
for tache in liste.afficherListe():
    print(tache.titre, "-", tache.description, "-", tache.statut)

# Affichage des tâches à faire
print("Tâches à faire :")
for tache in liste.filterListe('A FAIRE'):
    print(tache.titre, "-", tache.description, "-", tache.statut)



