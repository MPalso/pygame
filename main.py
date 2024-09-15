import pygame

#Inicializacia pygame
pygame.init()

#Vytvorenie obrazovky
width = 600
height = 300
screen = pygame.display.set_mode((width, height))

#Hlavny herny cyklus (aby sa okno stale vykreslovalo pokial ho nezavriem)
lets_continue = True

while lets_continue:
  for event in pygame.event.get():
    print(event)
    if event.type == pygame.QUIT:
      lets_continue = False
        

#Ukoncenie pygame
pygame.quit()