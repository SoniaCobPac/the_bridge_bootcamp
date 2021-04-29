class Orco():
    def __init__(self, nombre, armadura, nivel, ataque, salud=100, ojos=2, piernas=2, dientes=56):

        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.salud = salud
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes

    def atacar(self, humano):
        humano.salud = (humano.salud + humano.armadura) - self.ataque
        return humano.salud
        
    def no_vivo(self):
        if int(self.salud) <= 0:
            return True
        else:
            return False
    
    def atributos(self):
        print(f"Nombre: {self.nombre} | Armadura: {self.armadura} | Nivel: {self.nivel} | Ataque: {self.ataque} | Salud: {self.salud} \
            | Ojos: {self.ojos} | Piernas: {self.piernas} | Dientes: {self.dientes}")


