class Vehiculo:
    def __init__(self,modelo,color,marca): # corrected method name to __init__
        self.modelo = modelo
        self.color = color
        self.marca = marca
        # self.arrancado = false
        
moto = Vehiculo ("MT03", "negro", "Yamaha")

print(type(moto))

print(moto.modelo, moto.color, moto.marca)
