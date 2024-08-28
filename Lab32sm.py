class Mascota:
    def __init__(self,tamaño,color,raza): # corrected method name to __init__
        self.tamaño = tamaño
        self.color = color
        self.raza = raza
        # self.arrancado = false
        
gato = Mascota ("mediano", "blanco", "Persa")

print(type(gato))

print(gato.tamaño, gato.color , gato.raza)

