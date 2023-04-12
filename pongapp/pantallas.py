import pygame as pg
from pongapp.figura_class import Pelota, Raqueta
from .utils import *

class Partida:
    pg.init()
    def __init__(self):
        self.pantalla_principal=pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("PONG")
        self.tasa_refresco=pg.time.Clock()

        self.pelota = Pelota(ANCHO//2, ALTO//2)
        self.raqueta1 = Raqueta(0, ALTO//2)
        self.raqueta2 = Raqueta(ANCHO-15, ALTO//2)
         
        self.fuente = pg.font.Font(None, 30) #Inicializar fuente, con tipo de fuente y tamaño
        
        self.contadorDerecho = 0
        self.contadorIzquierdo = 0

        self.quienMarco = ""


    def bucle_fotrograma(self):
        game_over = False
        while not game_over:
            self.tasa_refresco.tick(300)

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True

            self.raqueta1.moverRaqueta(pg.K_w, pg.K_s)   
            self.raqueta2.moverRaqueta(pg.K_UP, pg.K_DOWN)
            self.quienMarco = self.pelota.moverPelota()
            
            self.pantalla_principal.fill(COLOR_CANCHA) 

            self.mostrar_linea_central()
        
            self.pelota.dibujarPelota(self.pantalla_principal)
            self.raqueta1.dibujarRaqueta(self.pantalla_principal)
            self.raqueta2.dibujarRaqueta(self.pantalla_principal)

            #logica de choque 
        
            self.pelota.comprobar_choqueV2(self.raqueta1, self.raqueta2)
   
            self.mostrar_marcador()

            self.mostrar_jugadores()
          

            pg.display.flip()
    
        pg.quit()

    def mostrar_jugadores(self):
        jugador1 = self.fuente.render("Player 1",True ,COLOR_PLAYER)
        jugador2 = self.fuente.render("Player 2",True , COLOR_PLAYER)
        self.pantalla_principal.blit(jugador1, (150, 20))
        self.pantalla_principal.blit(jugador2, (550, 20))
    
    def mostrar_linea_central(self):
        cont_linea = 10
        while cont_linea <= 600:
            pg.draw.line(self.pantalla_principal, BLANCO, (ANCHO//2 , cont_linea), (ANCHO//2 , cont_linea + 40), 8)
            cont_linea += 60

    def mostrar_marcador(self):
        if self.quienMarco == "right":
                self.contadorDerecho +=1
        elif self.quienMarco == "left":
                self.contadorIzquierdo += 1

        fuente = pg.font.Font(None, 100) #inicializar texto,( nombre fuente, tamaño)
        jugador1 = fuente.render(str(self.contadorIzquierdo),True ,BLANCO)
        jugador2 = fuente.render(str(self.contadorDerecho),True , BLANCO)
        self.pantalla_principal.blit(jugador1, (170, 50))
        self.pantalla_principal.blit(jugador2, (570, 50))

           