class Puente:
    def __init__(self,inicio, largo):
        self.inicio = inicio
        self.largo = largo

    def dibujarPuente(self):
        print(' ' * self.inicio + '=' * self.largo)
        