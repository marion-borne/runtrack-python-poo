class Commande:
    
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix):
        self.__plats_commandes[nom_plat] = prix

    def annuler_commande(self):
        self.__statut_commande = "annulée"

    def __calculer_total(self):
        return sum(self.__plats_commandes.values())

    def afficher_commande(self):
        total_a_payer = self.__calculer_total()
        print(f"La commande n°{self.__numero_commande} est d'un montant total de {total_a_payer}€")

    def calculer_tva(self, taux_tva):
        total_hors_taxes = self.__calculer_total()
        return total_hors_taxes * taux_tva / 100
    
commande = Commande(1)
commande.ajouter_plat("Pissaladière", 15)
commande.ajouter_plat("Taboulet", 7)
commande.afficher_commande()
print(f"La TVA est de {commande.calculer_tva(15)}€")
