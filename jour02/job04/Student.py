class Etudiant:
    def __init__(self, nom, prenom, num, credits=0):
        self.nom = nom
        self.prenom = prenom
        self.num = num
        self.credits = credits
        self.level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.credits += credits
            self.level = self.__studentEval()

    def __studentEval(self):
        if self.credits >= 90: 
            return "Excellent"
        elif self.credits >= 80: 
            return "Très bien"
        elif self.credits >= 70: 
            return "Bien"
        elif self.credits >= 60: 
            return "Passable"
        else: 
            return "Insuffisant"

    def studentInfo(self):
        print(f"Nom = {self.nom}\nPrénom = {self.prenom}\nid = {self.num}\nNiveau = {self.level}")

# Création de l'objet étudiant
john = Etudiant("John", "Doe", 145)

# Ajout de crédits
for _ in range(3):
    john.add_credits(25)

# Affichage des informations de l'étudiant
john.studentInfo()

