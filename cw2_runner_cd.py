import pygame
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f'{current_time}', 0, "White")
    score_rect = score_surface.get_rect(center=(300, 15))
    screen.blit(score_surface, score_rect)
    return current_time


def player_animation():
    global player_index, player_surf

    if player_rect.bottom < 350:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]


pygame.init()  # uruchomienie silnika pygame

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moja pierwsza gra")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 24)  # czcionka systemowa
player_gravity = 0
game_active = True
start_time = 0

background_surface = pygame.image.load('images_PG/background.png').convert()  # definicja tła
text_surface = font.render("Punkty: ", 1, "Black")  # definicja napisu
text_rect = text_surface.get_rect(center=(300, 15))

mashroom_surface = pygame.image.load('images_PG/mashroom.png').convert_alpha()  # definicja przeszkody
mashroom_rect = mashroom_surface.get_rect(bottomleft=(520, 350))  # opakowanie surface w prostokąt dla lepszego panowania

# grafiki pod animacje
player_walk_1 = pygame.image.load("images_PG/girl_walk.png").convert_alpha()
player_walk_2 = pygame.image.load("images_PG/girl_walk2.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load("images_PG/girl_jump.png").convert_alpha()

player_surf = player_walk[player_index]

# player_surface = pygame.image.load('images_PG/girl_stay.png').convert_alpha()
player_rect = player_surf.get_rect(bottomleft=(50, 350))

player_stay = pygame.image.load('images_PG/girl_stay.png').convert_alpha()
player_stay = pygame.transform.scale2x(player_stay)
player_stay_rect = player_stay.get_rect(center=(300, 200))

game_name = font.render("Witaj w mojej pierwszej grze", 0, "White")
game_name_rect = game_name.get_rect(center=(300, 15))

game_msg = font.render("Naciśnij spację, aby rozpocząć", 0, "White")
game_msg_rect = game_msg.get_rect(center=(300, 350))

# nieskończona pętla do przytrzymania okna gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # sprawdzenie jaki to typ zdarzenia
            pygame.quit()  # wyjście z gry
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom == 350:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
            if event.type == pygame.KEYDOWN and player_rect.bottom == 350:
                if event.key == pygame.K_SPACE:
                    # print("Skok")
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                mashroom_rect.x = 700
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(background_surface, (0, 0))  # wyświetlenie tła
        #pygame.draw.rect(screen, 'White', text_rect, 2)
        #pygame.draw.line(screen, "Red", (0, 0), pygame.mouse.get_pos(), 5)

        # screen.blit(text_surface, text_rect)  # wyświetlenie napisu
        score = display_score()

        mashroom_rect.x -= 5
        if mashroom_rect.x < -100:
            mashroom_rect.x = 700

        screen.blit(mashroom_surface, mashroom_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 350:
            player_rect.bottom = 350

        player_animation()
        screen.blit(player_surf, player_rect)

        # # skakanie - sposób 1
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print("skok")

        if player_rect.colliderect(mashroom_rect):
            # pygame.quit()
            # exit()
            game_active = False
    else:
        screen.fill("Black")
        # screen.blit(game_name, game_name_rect)  # wypisanie powitania

        score_msg = font.render(f'Twój wyniki to: {score}', False, "White")
        score_msg_rect = score_msg.get_rect(center=(300, 15))
        if score == 0:
            screen.blit(game_name, game_name_rect)
        else:
            screen.blit(score_msg, score_msg_rect)

        screen.blit(player_stay, player_stay_rect)  # grafika gracza
        screen.blit(game_msg, game_msg_rect)  # komenda


    pygame.display.update()  #aktualizacja obraz
    clock.tick(60)  # fps - jak czesto ma sie aktualizowac ekran (60 klatek na sekunde)
