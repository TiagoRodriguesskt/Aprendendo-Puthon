#PROGRAMA PARA TOCAR MUSICA

import pygame
pygame.mixer.init()
pygame.mixer.music.load('maisumdiasemvoce.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()