class Point:
    
    def __init__(self):
        self.x = 2
        self.y = 6
        
    def set_x(self, x):
        self.x = x
        
    def set_y(self, y):
        self.y = y
        
    def afficherLesPoints(self):
        print(f"Les coordonnées des points sont {self.x} et {self.y}")
        
    def afficherX(self):
        print(f'x est égal à {self.x}')
        
    def afficherY(self):
        print(f'y est égal à {self.y}')
        
    def changerX(self, x):
        self.x = x
        print(f'La nouvelle valeur de x est {self.x}')
        
    def changerY(self, y):
        self.y = y
        print(f'La nouvelle valeur de y est {self.y}')
        
        
calcul = Point()
calcul.afficherLesPoints()
calcul.afficherX()
calcul.afficherY()
calcul.changerX(12)
calcul.changerY(13)

