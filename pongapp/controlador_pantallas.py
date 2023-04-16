from .pantallas import *

class PantallaControlador:
    def __init__(self):
        self.menu = Menu()
        self.partida = Partida()
        self.resultado = Resultado()
        self.records = Records()
        self.resultado_final = "sadasdasdsf"

    def start(self):
        self.menu.bucle_pantalla()
        self.resultado_final = self.partida.bucle_pantalla()
        print(self.resultado_final)
        self.resultado.cargarResultado(self.resultado_final)
        self.resultado.bucle_pantalla()
        

