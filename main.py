#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import pygame
import sys
from pygame.locals import *
 
# Constantes o Variables
color = (234,234,234)
WIDTH = 850
HEIGHT = 480
window = pygame.display.set_mode((WIDTH,HEIGHT))
lista_de_BloquesA = []
lista_de_BloquesB = []
lista_de_BloquesC = []
lista_de_BloquesD = []
lista_de_BloquesE = []
lista_de_BloquesF = []

# ---------------------------------------------------------------------
 
# Clases
# ---------------------------------------------------------------------

class Bola(pygame.sprite.Sprite):
    """Comportamiento de la Bola"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("Imagenes/ball.png", True) # Ignored
        self.rect = self.image.get_rect()                  # Ignored
        self.rect.centerx = 425
        self.rect.centery = 450
        self.speed = [0.2, -0.2]
 

    def movimiento(self, time):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT or self.rect.colliderect(player.rect) or self.rect.colliderect(block.rect):
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time

    def destroy(self):
        pass


    def dibujar(self):
        pygame.draw.circle(window,(255,255,255),(self.rect.centerx, self.rect.centery),8)


# ---------------------------------------------------------------------

class Player(pygame.sprite.Sprite):
    """Comportamiento del Jugador"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagenes/player.png")
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT -10
        self.speed = 0
        self.aceleracion = 7
        
    def movimiento(self, direccion):
        if direccion == "NO":
            self.speed = 0

        elif direccion == "IZQUIERDA":
            self.speed = -self.aceleracion

        elif direccion == "DERECHA":
            self.speed = self.aceleracion
    

    def actualizar(self):
        self.rect.centerx += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 850:
            self.rect.right = 850


    def dibujar(self):
        window.blit(self.image, self.rect)

# ---------------------------------------------------------------------

class Block(pygame.sprite.Sprite):
    """Comportamiento de los Bloques"""
    def __init__(self, posX, posY, distance):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagenes/ball.png") # Ignored
        self.rect = self.image.get_rect()                   # Ignored
        self.centerx = posX
        self.centery = posY
        self.unbroken = True                                # Ignored
    
    def __destroying(self):
        pass

    def dibujar(self):
        self.block = pygame.draw.rect(window,color,(self.centerx,self.centery,75,20))


# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------

def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error:
                raise SystemExit
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

def cargarBloques():
    posX = 20
    for x in range(1,11):
        global block
        block = Block(posX,165,80)
        lista_de_BloquesA.append(block)
        posX = posX + 80

    posX = 100
    for x in range(1,9):
        block = Block(posX,135,80)
        lista_de_BloquesB.append(block)
        posX = posX + 80

    posX = 180
    for x in range(1,7):
        block = Block(posX,105,80)
        lista_de_BloquesC.append(block)
        posX = posX + 80

    posX = 260
    for x in range(1,5):
        block = Block(posX,75,80)
        lista_de_BloquesD.append(block)
        posX = posX + 80

    posX = 340
    for x in range(1,3):
        block = Block(posX,45,80)
        lista_de_BloquesE.append(block)
        posX = posX + 80

    posX = 380
    for x in range(1,2):
        block = Block(posX,15,80)
        lista_de_BloquesF.append(block)
        posX = posX + 80

# --------------------------------------------------------------------- 
 
def main():
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("BlockBreaker")

    icon = pygame.image.load("Imagenes/ball.ico")
    pygame.display.set_icon(icon)


    # Objetos principales
    global bola
    bola = Bola()
    global player
    player = Player()

    cargarBloques()

    clock = pygame.time.Clock()

 
    while True:
        window.fill((90,90,90))
        time = clock.tick(60)
        
        # Eventos de teclado
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    elif event.key == K_LEFT:
                        player.movimiento("IZQUIERDA")

                    elif event.key == K_RIGHT:
                        player.movimiento("DERECHA")

            elif event.type == KEYUP:
                    if event.key == K_LEFT:
                        player.movimiento("NO")

                    elif event.key == K_RIGHT:
                        player.movimiento("NO")



            

 
        bola.movimiento(time)
        bola.dibujar()
        player.actualizar()
        player.dibujar()


# ---------------------------------------------------------------------
 
# Renderización de Bloques | START
# ---------------------------------------------------------------------
        for i in lista_de_BloquesA:
            i.dibujar()
        
        for i in lista_de_BloquesB:
            i.dibujar()

        for i in lista_de_BloquesC:
            i.dibujar()

        for i in lista_de_BloquesD:
            i.dibujar()

        for i in lista_de_BloquesE:
            i.dibujar()

        for i in lista_de_BloquesF:
            i.dibujar()
        
# ---------------------------------------------------------------------
 
# Renderización de Bloques | END
# ---------------------------------------------------------------------
        
        
    
        pygame.display.update()

main()