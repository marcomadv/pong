import pygame as pg
from .utils import * 

class Raqueta:
    def __init__(self, pos_x, pos_y, w = 15, h = 100, color = BLANCO, vx = 1, vy = 1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h  
        self.color = color
        self.vx = vx
        self.vy = vy

    def dibujarRaqueta(self, pantalla):
        pg.draw.rect(pantalla, self.color,(self.pos_x, self.pos_y, self.w, self.h))

    def moverRaqueta(self, tecla_arriba, tecla_abajo, y_max = Y_MAX, y_min = Y_MIN):
        estado_teclado = pg.key.get_pressed()

        if estado_teclado[tecla_arriba] == True and self.pos_y > y_min:
            self.pos_y -= 3

    
        if estado_teclado[tecla_abajo] == True and self.pos_y < y_max - (self.h):
            self.pos_y += 3

    @property  # deja llamar a la funcion como una variable sin parentesis
    def derecha(self):
        return self.pos_x + (self.w//2)
    @property
    def izquierda(self):
        return self .pos_x - (self.w//2)
    @property
    def arriba(self):
        return self.pos_y - (self.h//2)
    @property
    def abajo(self):
        return self.pos_y + (self.h//2)
    

class Pelota:
    def __init__(self, pos_x, pos_y, color = COLOR_PELOTA, radio = 10, vx = 1, vy = 1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio
        self.vx = vx
        self.vy = vy

        self.contadorDerecho = 0
        self.contadorIzquierdo = 0

    def dibujarPelota(self, pantalla):
        pg.draw.circle(pantalla, self.color, (self.pos_x, self.pos_y,), self.radio)

    def moverPelota(self, x_max = X_MAX, y_max = Y_MAX, y_min = Y_MIN):
        self.pos_x += self.vx
        self.pos_y += self.vy

     
        if (self.pos_y >= y_max-self.radio) or (self.pos_y < 0 + self.radio): #rebote en eje y
            self.vy *= -1
        

        if self.pos_x >= x_max + self.radio *2: #limite derecha
            self.contadorIzquierdo +=1
            self.pos_x = x_max//2 #aparezca en el medio cuando se anota
            self.pos_y = y_max//2 #tambien pueda ir desde el medio hacia arriba
            self.vx *= -1
            self.vy *= -1
            

        if self.pos_x < y_min - self.radio *2 : #limite izquierdo
            self.contadorDerecho +=1
            self.pos_x = x_max//2
            self.pos_y = y_max//2        
            self.vx *= -1
            self.vy *= -1

    def mostrar_marcador(self, pantalla):
        fuente = pg.font.Font(None, 100) #inicializar texto,( nombre fuente, tamaño)
        jugador1 = fuente.render(str(self.contadorIzquierdo),True ,BLANCO)
        jugador2 = fuente.render(str(self.contadorDerecho),True , BLANCO)
        pantalla.blit(jugador1, (170, 50))
        pantalla.blit(jugador2, (570, 50))

    @property
    def derecha(self):
        return self.pos_x
    @property
    def izquierda(self):
        return self.pos_x - self.radio 
    @property
    def arriba(self):
        return self.pos_y - self.radio
    @property
    def abajo(self):
        return self.pos_y + self.radio

    def comprobar_choqueV2(self, *raquetas):
        for r in raquetas:
            if self.derecha >= r.izquierda and\
               self.izquierda <= r.derecha and\
               self.abajo >= r.arriba and\
               self.arriba <= r.abajo:
                    self.vx *= -1
