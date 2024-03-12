import pygame 
import random

# Establecemos ancho y alto
ANCHO = 1500
ALTO = 700

class slime(pygame.sprite.Sprite):
    # Funcion inicial
    def __init__(self):
        # inicializamos la variable
        super().__init__()

        # obtener la imagen de el slime
        self.image = pygame.image.load("slime.png") #/carpeta/fichero.png
        # obtener rectangulo de la imagen
        self.rect = self.image.get_rect()
        # aparicion de zombi
        self.rect.center = (0,450)
        
        self.aparicion_x = 20
        self.aparicion_y = 450
        # centramos el rectangulo
        self.radius = 22
        self.rect.x = random.randrange(self.aparicion_x - self.rect.x)

        # velocidad del slime
        
        self.slime_speed_x = random.randrange(2, 0 , -1, )
        self.slime_speed_y = int(random.randrange(3, -3 , -2, ))
    def update(self):
        # Actualizacion de velocidad

        self.rect.x += self.slime_speed_x
        self.rect.y += self.slime_speed_y

        puntuacion = 0
        # Limite de rango
        if self.rect.right > ANCHO:
            self.kill()
        if self.rect.bottom > ALTO:
            self.slime_speed_y = int(random.randrange(1, -3, -1))

        if self.rect.bottom < 500:
            self.slime_speed_y = int(random.randrange(3, 1, -1))
        if self.rect.right > ANCHO:
            puntuacion -= 1
