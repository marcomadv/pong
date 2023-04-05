import pygame as pg
from figura_class import Pelota, Raqueta

ANCHO = 800
ALTO = 600

class Partida:
    pg.init()
    def __init__(self):
        self.pantalla_principal=pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("PONG")
        self.tasa_refresco=pg.time.Clock()

        self.pelota = Pelota(ANCHO//2, ALTO//2)
        self.raqueta1 = Raqueta(0, ALTO//2)
        self.raqueta2 = Raqueta(ANCHO-15, ALTO//2)

    def bucle_fotrograma(self):
        game_over = False
        while not game_over:
            self.tasa_refresco.tick(300)

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True

            self.raqueta1.moverRaqueta(pg.K_w, pg.K_s)   
            self.raqueta2.moverRaqueta(pg.K_UP, pg.K_DOWN)
            self.pelota.moverPelota()

            self.pantalla_principal.fill((0, 0, 0)) #color negro rgb pantalla principal
            pg.draw.line(self.pantalla_principal, (255, 255, 255),(400, 0), (400, 600), width = 6)


            self.pelota.dibujarPelota(self.pantalla_principal)
            self.raqueta1.dibujarRaqueta(self.pantalla_principal)
            self.raqueta2.dibujarRaqueta(self.pantalla_principal)
    
            #logica de choque 
            self.pelota.comprobar_choqueV2(self.raqueta1, self.raqueta2)
   
            self.pelota.mostrar_marcador(self.pantalla_principal)

            pg.display.flip()
        

        pg.quit()

           