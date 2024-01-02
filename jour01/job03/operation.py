class operation:
    
    def __init__(self, nombre1 , nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
    def set_nombre1(self, nombre1):
        self.nombre1 = nombre1
        
    def set_nombre2(self, nombre2):
        self.nombre2 = nombre2
        
    def addition(self):
        result = self.nombre1 + self.nombre2
        print(f"l'addition du nombre {self.nombre1} et du nombre {self.nombre2} est égal à {result}")
        
        
calcul = operation(12, 3)
calcul.addition()