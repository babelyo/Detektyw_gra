import pygame
from sys import exit

pygame.init()  # uruchomienie silnika pygame

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moja pierwsza gra")
clock = pygame.time.Clock()

# nieskończona pętla do przytrzymania okna gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # sprawdzenie jaki to typ zdarzenia
            pygame.quit()  # wyjście z gry
            exit()


    pygame.display.update()  #aktualizacja obraz
    clock.tick(60)  # fps - jak czesto ma sie aktualizowac ekran (60 klatek na sekunde)
