import pygame as pg

class Raqueta:
    def __init__(self, pos_x, pos_y, w = 15, h = 100, color = (255, 255, 255), vx = 1, vy = 1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h  
        self.color = color
        self.vx = vx
        self.vy = vy

    def dibujarRaqueta(self, pantalla):
        pg.draw.rect(pantalla, self.color,(self.pos_x, self.pos_y, self.w, self.h))

    def moverRaqueta(self, tecla_arriba, tecla_abajo, y_max = 600, y_min = 0):
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
    def __init__(self, pos_x, pos_y, color = (255, 255, 255), radio = 10, vx = 1, vy = 1):
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

    def moverPelota(self, x_max = 800, y_max = 600, y_min = 0):
        self.pos_x += self.vx
        self.pos_y += self.vy

     
        if (self.pos_y >= y_max-self.radio) or (self.pos_y < 0 + self.radio): #rebote en eje y
            self.vy *= -1
        

        if self.pos_x >= x_max + self.radio * 5: #limite derecha
            self.vx *= -1
            self.contadorIzquierdo += 1

        if self.pos_x < y_min - self.radio * 5 : #limite izquierdo
            self.vx *= -1
            self.contadorDerecho += 1

    def mostrar_marcador(self, pantalla):
        fuente = pg.font.Font(None, 170) #inicializar texto,( nombre fuente, tamaño)
        jugador1 = fuente.render(str(self.contadorIzquierdo),True ,(255, 255, 255))
        jugador2 = fuente.render(str(self.contadorDerecho),True , (255, 255, 255))

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
    
    def comprobar_choque(self, r1, r2):
        if self.derecha >= r2.izquierda and\
            self.izquierda <= r2.derecha and\
            self.abajo >= r2.arriba and\
            self.arriba <= r2.abajo:
                self.vx *= -1 

        if self.derecha >= r1.izquierda and\
            self.izquierda <= r1.derecha and\
            self.abajo >= r1.arriba and\
            self.arriba <= r1.abajo:
                self.vx *= -1 
    
    



