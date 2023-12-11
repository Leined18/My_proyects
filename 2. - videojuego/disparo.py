import pygame
# Ubicamos la medidas
ANCHO = 1000
ALTO = 600

BLANCO = (255,255,255)
# Clase de disparo

class Disparo(pygame.sprite.Sprite):
    # Funcion inicial de la clase Disparo

    def __init__(self,x,y):
        # iniciamos la funcion inicial
        super().__init__()
        # Recolectar la imagen del disparo
        self.image = pygame.image.load("bala.png").convert()
        # Quitar fondo de bala al usar convert
        self.image.set_colorkey(BLANCO)
        # Tomar el rectangulo del sprite
        self.rect = self.image.get_rect()
        # Variable de movimiento
        self.rect.centerx = x
        self.rect.bottom = y
        # cadencia de disparos
        self.cadencia = 300
        # tomar el tiempo del ultimo disparo
        self.ultimate = pygame.time.get_ticks()
        

    def update(self):
        # Movimiento de la bala en X
        self.rect.x -=10

        # Limitante de borde

        if self.rect.right <0:
            self.kill()