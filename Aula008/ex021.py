# REPRODUZIR MP3
import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciar modulo
pygame.init()

pygame.mixer.music.load('ex021.mp3') #Carregar música no modulo
pygame.mixer.music.play(loops=0, start=0.0) #Tocar música
pygame.event.wait() #Aguardar música terminar de tocar

