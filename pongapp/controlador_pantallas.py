from .pantallas import *

class PantallaControlador:
    def __init__(self):
        self.pantalla=pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("PONG")
        self.tasa_refresco=pg.time.Clock()
        '''
        self.menu = Menu(self.pantalla, self.tasa_refresco)
        self.partida = Partida(self.pantalla, self.tasa_refresco)
        self.resultado = Resultado(self.pantalla, self.tasa_refresco)
        self.records = Records(self.pantalla, self.tasa_refresco)
        '''
        self.pantallas = [Menu(self.pantalla, self.tasa_refresco), Partida(self.pantalla, self.tasa_refresco), Resultado(self.pantalla, self.tasa_refresco), Records(self.pantalla, self.tasa_refresco)]

        self.resultado_final = ""

    def start(self):
        seguir = True
        indice = 0
        cerrar= ""
        while seguir: 
                          
                if indice ==0:
                    cerrar = self.pantallas[indice].bucle_pantalla()
                    if cerrar == True:
                        break
                indice +=1

                if indice ==1:
                    cerrar = self.pantallas[indice].bucle_pantalla()
               
                    if cerrar == True:
                        break
                    else:
                        self.resultado_final = cerrar  
                indice +=1
                
                if indice ==2:
                    self.pantallas[indice].cargarResultado(self.resultado_final)
                    cerrar = self.pantallas[indice].bucle_pantalla()
                    if cerrar == True:
                        break
                indice = 0
        '''
        seguir = True
        cerrar = ""
        while seguir:
            cerrar = self.menu.bucle_pantalla()
            if cerrar == True:
                break
            cerrar = self.partida.bucle_pantalla()
            if cerrar == True:
                break
            else:
                self.resultado_final = cerrar

            self.resultado.cargarResultado(self.resultado_final)

            cerrar = self.resultado.bucle_pantalla()
            if cerrar == True:
                break
        '''