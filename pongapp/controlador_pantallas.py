from .pantallas import *

class PantallaControlador:
    def __init__(self):
        self.menu = Menu()
        self.partida = Partida()
        self.resultado = Resultado()
        self.records = Records()

    def start(self):
        self.menu.bucle_pantalla()
        self.partida.bucle_pantalla()
        #resultado_final = self.partida.fin_de_partida()
        #if resultado_final != "":
          #  self.resultado.cargarResultado(resultado_final)
         #   self.resultado.bucle_pantalla()
        

