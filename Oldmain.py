import pygame as pg     
from pongapp.figura_class import Pelota, Raqueta    

pg.init()

pantalla_principal = pg.display.set_mode((800, 600))
pg.display.set_caption("Pong")


#definir tasa de refresco de nuestro bucle de fps
tasa_refresco = pg.time.Clock()

pelota = Pelota(400, 300)
raqueta1 = Raqueta(0, 300)
raqueta2 = Raqueta(785, 300)

game_over = False

while not game_over:
    #obtener tasa de refreso en milisengundos
    valor_tasa = tasa_refresco.tick(300) #variables para controlar la velocidad entre fotogramas (60 fps)
    #print(valor_tasa)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    raqueta1.moverRaqueta(pg.K_w, pg.K_s)   
    raqueta2.moverRaqueta(pg.K_UP, pg.K_DOWN)
    pelota.moverPelota()




    pantalla_principal.fill((0, 0, 0)) #color negro rgb pantalla principal
    pg.draw.line(pantalla_principal, (255, 255, 255),(400, 0), (400, 600), width = 6)

    pelota.dibujarPelota(pantalla_principal)
    raqueta1.dibujarRaqueta(pantalla_principal)
    raqueta2.dibujarRaqueta(pantalla_principal)
    
    #logica de choque 
    pelota.comprobar_choqueV2(raqueta1, raqueta2)
   
    '''
    if pelota.derecha >= raqueta2.izquierda and\
        pelota.izquierda <= raqueta2.derecha and\
        pelota.abajo >= raqueta2.arriba and\
        pelota.arriba <= raqueta2.abajo:
            pelota.vx *= -1 

    if pelota.derecha >= raqueta1.izquierda and\
        pelota.izquierda <= raqueta1.derecha and\
        pelota.abajo >= raqueta1.arriba and\
        pelota.arriba <= raqueta1.abajo:
            pelota.vx *= -1 
    
    '''
    pelota.mostrar_marcador(pantalla_principal)

    pg.display.flip()


pg.quit()