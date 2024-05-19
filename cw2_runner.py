import pygame
from sys import exit

pygame.init()  # uruchomienie silnika pygame

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moja pierwsza gra")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 24)  # czcionka systemowa
# font = pygame.font.Font('sciezka do pliku', 24) # swoja czcionka

# test_surface = pygame.Surface((50, 50))
# test_surface.fill("White")

background_surface = pygame.image.load('images_PG/background.png').convert()  # definicja tła
text_surface = font.render("Punkty: ", 1, "Black")  # definicja napisu

mashroom_surface = pygame.image.load('images_PG/mashroom.png').convert_alpha()  # definicja przeszkody
#mashroom_x_pos = 520
mashroom_rect = mashroom_surface.get_rect(bottomleft=(520, 350))  # opakowanie surface w prostokąt dla lepszego panowania

player_surface = pygame.image.load('images_PG/girl_stay.png').convert_alpha()
player_rect = player_surface.get_rect(bottomleft=(50, 350))

# nieskończona pętla do przytrzymania okna gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # sprawdzenie jaki to typ zdarzenia
            pygame.quit()  # wyjście z gry
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("zderzenie")
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print("nacisnieto")

    screen.blit(background_surface, (0, 0))  # wyświetlenie tła
    screen.blit(text_surface, (250, 10))  # wyświetlenie napisu

    mashroom_rect.x -= 5
    if mashroom_rect.x < -100:
        mashroom_rect.x = 700

    #screen.blit(mashroom_surface, (mashroom_x_pos, 300))
    screen.blit(mashroom_surface, mashroom_rect)

    screen.blit(player_surface, player_rect)

    # if player_rect.colliderect(mashroom_rect):
    #     print("zderzenie")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()  #aktualizacja obraz
    clock.tick(60)  # fps - jak czesto ma sie aktualizowac ekran (60 klatek na sekunde)
