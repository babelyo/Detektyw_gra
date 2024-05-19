import pygame
from sys import exit

pygame.init()  # uruchomienie silnika pygame

WIDTH, HEIGHT = 800, 400
x, y = 400, 200
step = 2
DARKRED = (85, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moja pierwsza gra")
clock = pygame.time.Clock()

# nieskończona pętla do przytrzymania okna gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # sprawdzenie jaki to typ zdarzenia
            pygame.quit()  # wyjście z gry
            exit()

    # pygame.draw.rect(screen, "White", (10, 10, 50, 100))
    # pygame.draw.rect(screen, DARKRED, (70, 10, 50, 100))
    #
    # pygame.draw.line(screen, "Red", (10, 120), (110, 120), 5)  #linia pozioma
    # pygame.draw.line(screen, "Blue", (10, 130), (10, 230), 5)  # linia pionowa
    #

    # for _ in range(WIDTH):
    #     for _ in range(HEIGHT):
    #         pygame.draw.rect(screen, DARKRED, (x + step, y + step, 10, 10))
    #         step += 10
    # TO DO - przekątna do narożnika lewy dół

    # print(pygame.key.get_pressed())

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= step
    if keys[pygame.K_RIGHT]:
        x += step
    if keys[pygame.K_UP]:
        y -= step
    if keys[pygame.K_DOWN]:
        y += step

    screen.fill("Black")
    pygame.draw.rect(screen, "White", (x, y, 10, 10))

    # wypisywanie tekstu na ekran
    # krok 1: definicja czcionki
    font = pygame.font.SysFont('Arial', 24)
    # krok 2: renderowanie czcionki
    label = font.render("Hello World", 1, "White")
    # krok 3: wyświetlnie na ekran
    screen.blit(label, (350, 30))

    pygame.display.update()  #aktualizacja obraz
    clock.tick(60)  # fps - jak czesto ma sie aktualizowac ekran (60 klatek na sekunde)
