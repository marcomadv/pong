import pygame as pg
from pongapp.figura_class import Pelota, Raqueta
from .utils import *

class Partida:
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

        self.resultado_partida = ""


    def bucle_pantalla(self):
        self.temporizador = TIEMPO
        self.tasa_refresco.tick()
        self.contadorDerecho = 0
        self.contadorIzquierdo = 0

        while not self.game_over and (self.contadorDerecho <10 or self.contadorIzquierdo< 10) and self.temporizador > 0:

            salto_tiempo = self.tasa_refresco.tick(FPS)
            self.fin_de_partida()
            self.temporizador -= salto_tiempo

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return  True

            self.raqueta1.moverRaqueta(pg.K_w, pg.K_s)   
            self.raqueta2.moverRaqueta(pg.K_UP, pg.K_DOWN)
            self.quienMarco = self.pelota.moverPelota()
            
            self.pantalla_principal.fill(COLOR_CANCHA) 

            self.mostrar_linea_central()
        
            self.pelota.dibujarPelota(self.pantalla_principal)
            self.raqueta1.dibujarRaqueta(self.pantalla_principal)
            self.raqueta2.dibujarRaqueta(self.pantalla_principal)         
        
            self.pelota.comprobar_choque(self.raqueta1, self.raqueta2)

            self.mostrar_marcador()
            self.mostrar_temporizador()
            self.mostrar_jugadores()
          

            pg.display.flip()

        return self.resultado_partida

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
        if self.contadorDerecho > self.contadorIzquierdo:
            self.resultado_partida = f"Gana el jugador 2, resultado jugador2: {self.contadorDerecho}, resultado jugador1:{self.contadorIzquierdo}"
        elif self.contadorIzquierdo > self.contadorDerecho:
            self.resultado_partida = f"Gana el jugador 1, resultado jugador1: {self.contadorIzquierdo}, resultado jugador2:{self.contadorDerecho}"
        else:
            self.resultado_partida = "¡¡EMPATE!!"

        '''
        if self.temporizador <= 0:
            self.game_over = True
            if self.contadorDerecho > self.contadorIzquierdo:
                self.resultado_partida = f"Gana el jugador 2, resultado jugador2: {self.contadorDerecho}, jugador1:{self.contadorIzquierdo}"
            elif self.contadorDerecho < self.contadorIzquierdo:
                self.resultado_partida = f"Gana el jugador 1, resultado jugador1: {self.contadorIzquierdo}, jugador2:{self.contadorDerecho}"
            else:
                self.resultado_partida = "¡EMPATE!"

        # para que finalice el juego por puntos
        if self.contadorDerecho == 10:
            self.game_over = True
            self.resultado_partida = "Gana el jugador 1"
            
        if self.contadorIzquierdo == 10:
            self.game_over = True
            self.resultado_partida = "Gana el jugador 2"
        '''
            
class Menu:
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("MENU")
        self.tasa_refresco = pg.time.Clock()
        self.imagenFondo = pg.image.load(IMG_FONDO)
        self.fuenteMenu = pg.font.Font(FUENTE, 25)
        self.sonido = pg.mixer.Sound(SONIDO_AMBIENTE)

    def bucle_pantalla(self):
        self.tasa_refresco.tick(FPS)
        game_over = False 
        pg.mixer.Sound.play(self.sonido) #iniciamos el sonido 

        while not game_over:
            for evento in pg.event.get():
                  if evento.type == pg.QUIT:
                       return True
                  
                  if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True

            '''
            if boton[pg.K_RETURN] == True:
                game_over = True
                pg.mixer.Sound.stop(self.sonido)
                return "partida"
            if boton[pg.K_SPACE] == True:
                game_over = True
                pg.mixer.Sound.stop(self.sonido)
                return "records"
            '''
                  
            self.pantalla_principal.blit(self.imagenFondo,(0, 0))
            jugar = self.fuenteMenu.render("Pulsa ENTER para jugar", 0, AZUL)
            records = self.fuenteMenu.render("Pulsa ESPACE para puntos", 0, AZUL)

        

            self.pantalla_principal.blit(jugar, (155, ALTO//2))
            self.pantalla_principal.blit(records, (155, 350))
    

            pg.display.flip()

        pg.mixer.Sound.stop(self.sonido)


class Resultado:
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("RESULTADOS")
        self.tasa_refresco = pg.time.Clock()
        self.fuenteResultado = pg.font.Font(FUENTE, 10)
        self.resultado_final = "" 
    
          
    def bucle_pantalla(self):
        self.tasa_refresco.tick(FPS)
        game_over = False

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
                
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True
                
            self.pantalla_principal.fill(BLANCO)
            resultado = self.fuenteResultado.render(self.resultado_final, 0, NARANJA)

            self.pantalla_principal.blit(resultado, (130, ALTO//2))
            
            pg.display.flip()
        
  

    def cargarResultado(self, resultado):
        self.resultado_final = resultado
        
        return self.resultado_final

class Records:
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("RECORDS")
        self.tasa_refresco = pg.time.Clock()
        self.fuenteRecords = pg.font.Font(FUENTE, 15)

    def bucle_pantalla(self):
        self.tasa_refresco.tick(FPS)
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                  if evento.type == pg.QUIT:
                       return True
                  
                  if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True
        
            self.pantalla_principal.fill(BLANCO)
            texto = self.fuenteRecords.render("Mejores puntuaciones", 0, AZUL)

            self.pantalla_principal.blit(texto, (155, ALTO//2))


            pg.display.flip()


