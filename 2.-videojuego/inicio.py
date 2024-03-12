import pygame

from slime import slime
from disparo import Disparo

# Dimensiones de la ventana
ANCHO = 1500
ALTO = 700
# control de FPS
FPS = 60
# Fuentes 
consolas = pygame.font.match_font('consolas')
time = pygame.font.match_font("time")
arial = pygame.font.match_font("arial")
courier = pygame.font.match_font("courier")



# colores
NEGRO = (0,0,0)
ROJO = (255,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
# clase personaje
class player(pygame.sprite.Sprite):
    # inicializamos la funcion
    def __init__(self):
        # inicializamos funcion
        super().__init__()
        # Obtenemos imagen del personaje
        self.image = pygame.image.load("player.png")
        # obtenemos el rectangulo (sprite)
        self.rect = self.image.get_rect()
        # aparicion de personaje
        self.rect.center = (ANCHO, 550)
        # Velocidad del personaje
        self.velocidad_x = 0
        self.velocidad_y = 0
        # cadencia de disparos
        self.cadencia = 500
        # tomar el tiempo del ultimo disparo
        self.ultimate = pygame.time.get_ticks()

    def update(self):
        self.velocidad_x = 0
        self.velocidad_y = 0

        # variable para detectar las pulsacion de las teclas
        teclas = pygame.key.get_pressed()
        # Configuracion del teclado
        if teclas[pygame.K_a]:
            self.velocidad_x = -3
        if teclas[pygame.K_d]:
            self.velocidad_x = +3
        if teclas[pygame.K_s]:
            self.velocidad_y = +3
        if teclas[pygame.K_w]:
            self.velocidad_y = -3
        if teclas[pygame.K_SPACE]:
            # tomamos el ultimo tiempo de salida del disparo
            tiempo = pygame.time.get_ticks()
            # sentencia de disparos
            if tiempo - self.ultimate > self.cadencia:
                self.fire()
                self.ultimate = tiempo
            

        # Actualizacion de velocidad
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
       

        # limites de bordes 
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > ANCHO:
            self.rect.right = ANCHO

        if self.rect.bottom < 500:
            self.rect.bottom = 500

        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
    
    def fire(self):
        fires = Disparo(self.rect.centerx -59, self.rect.centery -32)
        disparos.add(fires)


#clase inicio
class Inicio ():
    # Inicializacion de videojuego
    pygame.init()

# ambiente
ambiente = pygame.mixer.music.load('final_song.mp3')
ambiente = pygame.mixer.music.load('ambiente.wav')

pygame.mixer.music.queue("ambiente.wav")
pygame.mixer.music.queue("final_song.mp3")
pygame.mixer.music.play(-1)

# efectos de sonido
GameOver_sound = pygame.mixer.Sound("gamveover.wav")
slime_death = pygame.mixer.Sound("slime_death.wav")
win_sound = pygame.mixer.Sound("win.wav")
# Creacion de la pantalla

Pantalla = pygame.display.set_mode((ANCHO,ALTO))

# Aplicacion de fondo

Fondo = pygame.transform.scale(pygame.image.load("Mapa_1.jpg").convert(),(1500,700))

# nombre de la ventana de nuestro videojuego

pygame.display.set_caption("Shooter Fire")

# variable para tomar el tiempo en el videojuego

time = pygame.time.Clock()

# Puntuacion

puntuacion = 10

# funcion para crear textos
def Texto(pantalla,fuente,texto,color,dimensiones,x,y):
    tipo_letra = pygame.font.Font(fuente,dimensiones)
    superficie = tipo_letra.render(texto,True,color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x,y)
    pantalla.blit(superficie,rectangulo)

# creacion de sprites 

slimes = pygame.sprite.Group()
jugador = pygame.sprite.Group()
disparos = pygame.sprite.Group()

# inicializamos jugador
players = player()
jugador.add(players)
# La variable game over indica la iniciacion del juego

GameOver = False

# evaluamos en el ciclo

while GameOver == False:
    # controlador de FPS
    time.tick(FPS)

    # Establecemos el fondo a la pantalla
    Pantalla.blit(Fondo,(0,0))

    # Detectar el ciclo y eventos dentro del videojuego
    for event in pygame.event.get():
        
        # si el jugador da clic al boton de "cerrar ventana" la ventana se cerrara y el juego terminara
        if event.type == pygame.QUIT:
            # la variable pasa a tener el valor de true
            GameOver = True
    
    # colisiones de sprite
    colision_bala = pygame.sprite.groupcollide(slimes,disparos,True,True)
    colision_slime = pygame.sprite.groupcollide(slimes,jugador,False,False)

    # muestra de puntos en pantalla
    Texto(Pantalla,consolas,str(puntuacion),ROJO,50,1430,67)
    # muestra de meta en pantalla
    Texto(Pantalla,consolas,str("Goal:2000"),ROJO,50,150,67)
    # condiciones de colision

    if colision_bala:
        puntuacion += 5
        pygame.mixer.Sound.play(slime_death)

    if colision_slime:
        puntuacion -= 5

    if puntuacion <= 0:
        Pantalla.fill(NEGRO)
        Texto(Pantalla,arial,"GAME OVER",ROJO,200,700,400)
        pygame.display.update()
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(GameOver_sound)
        players.kill()

    if puntuacion >= 2000:
        Pantalla.fill(BLANCO)
        enemigos = 0
        Texto(Pantalla,arial,"YOU WON",VERDE,200,700,400)
        pygame.display.update()
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(win_sound)
        enemy.kill()
        players.kill()
        

    

    # Cantidad de enemigos
    enemigos = 5 
    # se actualiza el parametro de pygame
    
    slimes.update()
    players.update()
    disparos.update()
    # Aparicion aleatoria de enemigos 
    
    if puntuacion >= 100:
        enemigos += 2
    if puntuacion >= 500:
        enemigos += 3
    if puntuacion >= 1000:
        enemigos += 3
    if puntuacion >= 1500:
        enemigos += 7
    if puntuacion >= 2000:
        enemigos = 0

    if puntuacion > 0:
        if not slimes:
            for x in range(enemigos):
                enemy = slime()
                slimes.add(enemy)
    
    slimes.draw(Pantalla)
    jugador.draw(Pantalla)
    disparos.draw(Pantalla)
    pygame.display.flip()
            
    

