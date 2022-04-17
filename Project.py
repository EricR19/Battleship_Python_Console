class Game:
    def __init__(self, puntos, vida):
        self.puntos = int(puntos)
        self.vida = vida

    def saludo(self):
        print("Hello " + str(self.puntos))


p1 = Game(35, 100)
p1.saludo()
