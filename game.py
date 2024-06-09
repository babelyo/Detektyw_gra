import pygame
from sys import exit

pygame.init()  # uruchomienie silnika pygame

WIDTH, HEIGHT = 1600, 900
step = 1

first_locations = pygame.image.load('office/background.png')
menu_background = pygame.image.load('office/menu_background.png')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Detektyw")
clock = pygame.time.Clock()

player_frames = []
for i in range(47):
    frame_path = f'detective/{i:02d}_detective.png'
    player_frames.append(pygame.image.load(frame_path))


current_scene = "menu"

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, frames, obstacles):
        super().__init__()
        self.frames = frames
        self.current_frame = 16
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.animation_speed = 0.2
        self.obstacles = obstacles

    def update(self):
        last_x, last_y = self.rect.x, self.rect.y

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.current_frame += self.animation_speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.current_frame += self.animation_speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
            self.current_frame += self.animation_speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
            self.current_frame += self.animation_speed

        current_x, current_y = self.rect.x, self.rect.y

        if pygame.sprite.spritecollide(self, self.obstacles, False):
            self.rect.x, self.rect.y = last_x, last_y

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 40:
            self.rect.top = 40
        if self.rect.bottom > 880:
            self.rect.bottom = 880

        if last_x < current_x and last_y == current_y:
            if self.current_frame >= 39 or self.current_frame < 32:
                self.current_frame = 32
            self.image = self.frames[int(self.current_frame)]
        elif last_x > current_x and last_y == current_y:
            if self.current_frame >= 47 or self.current_frame < 40:
                self.current_frame = 40
            self.image = self.frames[int(self.current_frame)]
        if last_y > current_y:
            if self.current_frame >= 31 or self.current_frame < 24:
                self.current_frame = 24
            self.image = self.frames[int(self.current_frame)]
        elif last_y < current_y:
            if self.current_frame >= 24 or self.current_frame < 16:
                self.current_frame = 16
            self.image = self.frames[int(self.current_frame)]

        self.image = pygame.transform.scale_by(self.frames[int(self.current_frame)], 3)
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale_by(self.image, 3)
        self.rect = self.image.get_rect(center=(x, y))
        self.rect.x = x
        self.rect.y = y


class Board(Obstacle):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)


class Place_with_items():
    def __init__(self, x, y, image):
        super().__init__(x, y, image)


class Item:
    def __init__(self, name, image):
        self.name = name
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()



dummy_obstacles = pygame.sprite.Group()
dummy_obstacles.add(Obstacle(1200, 600, "office/STOL.png"))
dummy_obstacles.add(Obstacle(1190, 710, "office/Sofa_s.png"))
dummy_obstacles.add(Obstacle(1390, 570, "office/Sofa_e.png"))
dummy_obstacles.add((Obstacle(850, 150, "office/szafka.png")))
dummy_obstacles.add((Obstacle(855, 55, "office/gramofon.png")))
dummy_rack_y = 100
for _ in range(6):
    dummy_obstacles.add((Obstacle(20, dummy_rack_y, "office/szafka_w.png")))
    dummy_rack_y += 85

board = Board(300, 50, "office/board.png")

player = Player(800, 450, player_frames, dummy_obstacles)
all_sprites = pygame.sprite.Group()
all_sprites.add(dummy_obstacles)
all_sprites.add(board)
all_sprites.add(player)


def game_scene():
    global current_scene
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # sprawdzenie jaki to typ zdarzenia
            pygame.quit()  # wyjście z gry
            exit()

    background_image = pygame.transform.scale(first_locations, (WIDTH, HEIGHT)).convert_alpha()
    screen.blit(background_image, (0, 0))
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()  # aktualizacja obraz
    print(player.rect.x, player.rect.y)
    clock.tick(60)  # fps - jak czesto ma sie aktualizowac ekran (60 klatek na sekunde)

def control_scene():
    global current_scene
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  # Przechodzenie do gry po naciśnięciu ENTER
                current_scene = "menu"

    background_image = pygame.transform.scale(menu_background, (WIDTH, HEIGHT)).convert_alpha()
    screen.blit(background_image, (0, 0))
    font = pygame.font.Font(None, 74)
    text = font.render("W = Do góry", True, (0, 255, 255))
    text1 = font.render("S = W dół", True, (0, 255, 255))
    text2 = font.render("A = W lewo", True, (0, 255, 255))
    text3 = font.render("D = W prawo", True, (0, 255, 255))
    text4 = font.render("E = Użyj", True, (0, 255, 255))
    text5 = font.render("1. Cofnij", True, (0, 255, 255))
    screen.blit(text, (100, 200))
    screen.blit(text1, (100, 300))
    screen.blit(text2, (100, 400))
    screen.blit(text3, (100, 500))
    screen.blit(text4, (100, 600))
    screen.blit(text5, (1400, 850))
    pygame.display.update()


def menu_scene():
    global current_scene
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  # Przechodzenie do gry po naciśnięciu ENTER
                current_scene = "game"
            if event.key == pygame.K_3:
                current_scene = "control"
            if event.key == pygame.K_4:
                pygame.quit()
                exit()

    background_image = pygame.transform.scale(menu_background, (WIDTH, HEIGHT)).convert_alpha()
    screen.blit(background_image, (0, 0))
    font = pygame.font.Font(None, 74)
    text = font.render("1.Nowa gra", True, (0, 255, 255))
    text1 = font.render("2.Wczytaj grę", True, (0, 255, 255))
    text2 = font.render("3.Sterowanie", True, (0, 255, 255))
    text3 = font.render("4.Wyjście", True, (0, 255, 255))
    screen.blit(text, (700, 200))
    screen.blit(text1, (700, 300))
    screen.blit(text2, (700, 400))
    screen.blit(text3, (700, 500))
    pygame.display.update()


while True:
    if current_scene == "menu":
        menu_scene()
    elif current_scene == "game":
        game_scene()
    elif current_scene == "control":
        control_scene()