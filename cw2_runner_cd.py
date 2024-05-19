import pygame
from sys import exit

pygame.init()  # uruchomienie silnika pygame

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moja pierwsza gra")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 24)  # czcionka systemowa
player_gravity = 0

background_surface = pygame.image.load('images_PG/background.png').convert()  # definicja tła
text_surface = font.render("Punkty: ", 1, "Black")  # definicja napisu
text_rect = text_surface.get_rect(center=(300, 15))

mashroom_surface = pygame.image.load('images_PG/mashroom.png').convert_alpha()  # definicja przeszkody
mashroom_rect = mashroom_surface.get_rect(bottomleft=(520, 350))  # opakowanie surface w prostokąt dla lepszego panowania

player_surface = pygame.image.load('images_PG/girl_stay.png').convert_alpha()
player_rect = player_surface.get_rect(bottomleft=(50, 350))

# nieskończona pętla do przytrzymania okna gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # sprawdzenie jaki to typ zdarzenia
            pygame.quit()  # wyjście z gry
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom == 350:
            if player_rect.collidepoint(event.pos):
                player_gravity = -20
        if event.type == pygame.KEYDOWN and player_rect.bottom == 350:
            if event.key == pygame.K_SPACE:
                # print("Skok")
                player_gravity = -20

    screen.blit(background_surface, (0, 0))  # wyświetlenie tła
    #pygame.draw.rect(screen, 'White', text_rect, 2)
    #pygame.draw.line(screen, "Red", (0, 0), pygame.mouse.get_pos(), 5)

    screen.blit(text_surface, text_rect)  # wyświetlenie napisu

    mashroom_rect.x -= 5
    if mashroom_rect.x < -100:
        mashroom_rect.x = 700

    screen.blit(mashroom_surface, mashroom_rect)

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 350:
        player_rect.bottom = 350
    screen.blit(player_surface, player_rect)

    # # skakanie - sposób 1
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("skok")

    if player_rect.colliderect(mashroom_rect):
        pygame.quit()
        exit()

    pygame.display.update()  #aktualizacja obraz
    clock.tick(60)  # fps - jak czesto ma sie aktualizowac ekran (60 klatek na sekunde)
