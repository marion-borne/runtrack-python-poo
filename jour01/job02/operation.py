class operation:
    
    def __init__(self, nombre1 , nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
    def set_nombre1(self, nombre1):
        self.nombre1 = nombre1
        
    def set_nombre2(self, nombre2):
        self.nombre2 = nombre2
        
    def __str__(self):
        return f"le nombre1 est {self.nombre1}, le nombre2 est {self.nombre2}"
        
        
calcul = operation(12, 3)
print(calcul)