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
         
        self.fuente = pg.font.Font(FUENTE, 20) #Inicializar fuente, con tipo de fuente y tamaño
        
        self.contadorDerecho = 0
        self.contadorIzquierdo = 0

        self.quienMarco = ""

        self.temporizador = TIEMPO
        self.game_over = False


    def bucle_fotrograma(self):
        game_over = False

        while not self.game_over:
            salto_tiempo = self.tasa_refresco.tick(300)
            self.fin_de_partida()
            self.temporizador -= salto_tiempo

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    self.game_over = True

            self.raqueta1.moverRaqueta(pg.K_w, pg.K_s)   
            self.raqueta2.moverRaqueta(pg.K_UP, pg.K_DOWN)
            self.quienMarco = self.pelota.moverPelota()
            
            self.pantalla_principal.fill(COLOR_CANCHA) 

            self.mostrar_linea_central()
        
            self.pelota.dibujarPelota(self.pantalla_principal)
            self.raqueta1.dibujarRaqueta(self.pantalla_principal)
            self.raqueta2.dibujarRaqueta(self.pantalla_principal)         
        
            self.pelota.comprobar_choqueV2(self.raqueta1, self.raqueta2)

            self.mostrar_marcador()
            self.mostrar_temporizador()
            self.mostrar_jugadores()
          

            pg.display.flip()
    
        pg.quit()

    def mostrar_jugadores(self):
        jugador1 = self.fuente.render("Player 1",True ,COLOR_PLAYER)
        jugador2 = self.fuente.render("Player 2",True , COLOR_PLAYER)
        self.pantalla_principal.blit(jugador1, (120, 20))
        self.pantalla_principal.blit(jugador2, (520, 20))
    
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

        fuente = pg.font.Font(FUENTE, 50) #inicializar texto,( nombre fuente, tamaño)
        jugador1 = fuente.render(str(self.contadorIzquierdo),True ,BLANCO)
        jugador2 = fuente.render(str(self.contadorDerecho),True , BLANCO)
        self.pantalla_principal.blit(jugador1, (170, 55))
        self.pantalla_principal.blit(jugador2, (570, 55))

    def mostrar_temporizador(self):
         tiempo_juego= self.fuente.render(str(self.temporizador//1000),0,AZUL)
         if self.temporizador <= 11000:
              tiempo_juego= self.fuente.render(str(self.temporizador//1000),0,NARANJA)
         if self.temporizador <= 6000:
              tiempo_juego= self.fuente.render(str(self.temporizador//1000),0,ROJO)
              
         self.pantalla_principal.blit(tiempo_juego, (380, 51))
    
    def fin_de_partida(self):
        if self.temporizador <= 0:
            self.game_over = True

        # para que finalice el juego por puntos
        if self.contadorDerecho == 7:
            self.game_over = True
            print("El gandor es el jugador 2")
            
        if self.contadorIzquierdo == 7:
            self.game_over = True
            print("El ganador es el jugador 1")

class Menu:
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("MENU")
        self.tasa_refresco = pg.time.Clock()
        self.imagenFondo = pg.image.load("pongapp/images/fondo.jpg")
        self.fuenteMenu = pg.font.Font(FUENTE, 25)

    def bucle_pantalla(self):
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                  if evento.type == pg.QUIT:
                       game_over = True
        
            self.pantalla_principal.blit(self.imagenFondo,(0, 0))
            menu = self.fuenteMenu.render("Pulsa ENTER para jugar", 0, AZUL)
            self.pantalla_principal.blit(menu, (155, ALTO//2))

            pg.display.flip()

        pg.quit()
    