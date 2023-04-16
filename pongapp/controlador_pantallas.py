from .pantallas import *

class PantallaControlador:
    def __init__(self):
        self.menu = Menu()
        self.partida = Partida()
        self.resultado = Resultado()
        self.records = Records()
        self.resultado_final = ""

    def start(self):
        seguir = True
        cerrar = ""
        while seguir:
            cerrar = self.menu.bucle_pantalla()
            if cerrar == True:
                break
            

            '''
            self.resultado_final = self.partida.bucle_pantalla()
            self.resultado.cargarResultado(self.resultado_final)
            self.resultado.bucle_pantalla()
            '''