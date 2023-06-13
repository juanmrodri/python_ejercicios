import pygame, sys
from config import *

gravedad = True

movimiento_horizontal = True

pygame.init()

reloj = pygame.time.Clock()



ventana = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Titulo del juego")

player_1 = pygame.Surface((120,80))

player_1.fill(ROJO)

rect_player_1 = player_1.get_rect()

rect_player_1.center = CENTER

player_2 = pygame.Surface((120,80))

player_2.fill(VERDE)

rect_player_2 = player_2.get_rect()

rect_player_2.center = CENTER

#rect_1 = pygame.rect.Rect(100,70,120,60)

while True:

    reloj.tick(FPS)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            pygame.quit()
            sys.exit() # con esto le avisamos al sistema que cierre la ventana, de la parte del hardware

    # para pegar una superficie en otra, usamos el metodo blit(), por ej, un personaje en la ventana

    ventana.fill(NEGRO)

    ventana.blit(player_1, rect_player_1)

    ventana.blit(player_2, rect_player_2)

    if gravedad:

        if rect_player_1.bottom <= HEIGHT:

            rect_player_1.y += SPEED

        else:

            gravedad = not gravedad

    else:

        if rect_player_1.top >= 0:

            rect_player_1.y -= SPEED

        else:

            gravedad = not gravedad

    if movimiento_horizontal:

        if rect_player_2.right <= WIDTH:

            rect_player_2.x += SPEED

        else:

            movimiento_horizontal = not movimiento_horizontal

    else:

        if rect_player_2.left >= 0:

            rect_player_2.x -= SPEED

        else:

            movimiento_horizontal = not movimiento_horizontal

    

    # pygame.draw.rect(ventana,AMARILLO,rect_1)

    # rect_circle = pygame.draw.circle(ventana,AZUL, CENTER, 75)

    # pygame.draw.line(ventana,VERDE,(0 ,HEIGHT), (WIDTH, 0), 3)

    # pygame.draw.line(ventana,VERDE, CENTER, (WIDTH, HEIGHT), 3)

    # pygame.draw.line(ventana,VERDE, rect_1.topright, rect_circle.center, 3)

    # pygame.draw.polygon(ventana,ROJO,[(100,200), (150, 300), (50, 300)])

    pygame.display.flip() # esto es mostrar la pantalla, para eso es el metodo flip()