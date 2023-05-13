from pygame import *
from random import randint
win = display.set_mode((900, 600))
display.set_caption('Не_Пифики_Пафики')
bg = transform.scale(image.load('backg.png'), (900,600))
game = True
finish = False
speed_x = 5
speed_y = 3
speed_x1 = 7
speed_y1 = 5
score_l = 0
score_r = 0
font.init()
r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)
clock = time.Clock()
FPS = 60
text = font.Font(None, 48)
points_l = text.render(str(score_l), 1, (r, g, b))
points_r = text.render(str(score_r), 1, (r, g, b))

class GameSprite(sprite.Sprite):
    def __init__(self, pic, speed, x, y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(pic), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def get_placed(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, pic, speed, x, y, size_x, size_y, p_num, invert):
        super().__init__(pic, speed, x, y, size_x, size_y)
        self.num = p_num
        self.dir = int(invert)
    def get_moving(self):
        keys = key.get_pressed()
        if self.dir == 0: 
            if self.num == 1 and keys[K_w] and self.rect.y >= 20:
                self.rect.y -= self.speed
            if self.num == 1 and keys[K_s] and self.rect.y <= 430:
                self.rect.y += self.speed
            if self.num == 2 and keys[K_UP] and self.rect.y >= 20:
                self.rect.y -= self.speed
            if self.num == 2 and keys[K_DOWN] and self.rect.y <= 430:
                self.rect.y += self.speed
        if self.dir == 1:
            if self.num == 1 and keys[K_w] and self.rect.y <= 435:
                self.rect.y += self.speed
            if self.num == 1 and keys[K_s] and self.rect.y >= 15:
                self.rect.y -= self.speed
            if self.num == 2 and keys[K_UP] and self.rect.y <= 435:
                self.rect.y += self.speed
            if self.num == 2 and keys[K_DOWN] and self.rect.y >= 15:
                self.rect.y -= self.speed

rocket1 = Player('rock1.png', 10, 50, 100, 50, 150, 1, 0)
rocket2 = Player('rock2.png', 10, 800, 400, 50, 150, 2, 0)
ball = GameSprite('balls.png', 10, 450, 300, 75, 75)
ball2 = GameSprite('balls.png', 10, 450, 300, 75, 75)
while game:
    if score_l >= 3 or score_r >= 3:
        if speed_x == 5:
            speed_x = 7
        elif speed_x == -5:
            speed_x = -7
        if speed_y == 3:
            speed_y = 5
        elif speed_y == -3:
            speed_y == -5
        rocket1.speed = 15
        rocket2.speed = 15
    if score_l >= 10 and rocket1.dir == 0:
        rocket1.dir = 1
    if score_r >= 10 and rocket2.dir == 0:
        rocket2.dir = 1
    keys = key.get_pressed()
    clock.tick(FPS)
    win.blit(bg, (0,0))
    rocket1.get_placed()
    rocket2.get_placed()
    ball.get_placed()
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    win.blit(points_l, (200, 50))
    win.blit(points_r, (700, 50))
    points_l = text.render(str(score_l), 1, (r, g, b))
    points_r = text.render(str(score_r), 1, (r, g, b))
    if not(keys[K_SPACE]):
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    rocket1.get_moving()
    rocket2.get_moving()
    if ball.rect.y <= 25 or ball.rect.y >= 525:
        speed_y *= -1
    if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(ball, rocket2):
        speed_x *= -1
    if ball2.rect.y <= 25 or ball2.rect.y >= 525:
        speed_y1 *= -1
    if sprite.collide_rect(rocket1, ball2) or sprite.collide_rect(ball2, rocket2):
        speed_x1 *= -1
    if ball.rect.x >= 900 or ball2.rect.x >= 900:
        score_l += 1
        finish = False
        rocket1 = Player('rock1.png', 10, 50, 100, 50, 150, 1, 0)
        rocket2 = Player('rock2.png', 10, 800, 400, 50, 150, 2, 0)
        ball = GameSprite('balls.png', 10, 350, 250, 75, 75,)
        ball2 = GameSprite('balls.png', 10, 550, 350, 75, 75)
        rocket1.get_placed()
        rocket2.get_placed()
        ball.get_placed()
    if ball.rect.x <= -80 or ball2.rect.x <= -80:
        score_r += 1
        finish = False
        rocket1 = Player('rock1.png', 10, 50, 100, 50, 150, 1, 0)
        rocket2 = Player('rock2.png', 10, 800, 400, 50, 150, 2, 0)
        ball = GameSprite('balls.png', 10, 450, 300, 75, 75,)
        ball2 = GameSprite('balls.png', 10, 450, 300, 75, 75)
        rocket1.get_placed()
        rocket2.get_placed()
        ball.get_placed()
    if keys[K_r]:
        score_l = 0
        score_r = 0
        finish = False
        rocket1 = Player('rock1.png', 10, 50, 100, 50, 150, 1, 0)
        rocket2 = Player('rock2.png', 10, 800, 400, 50, 150, 2, 0)
        ball = GameSprite('balls.png', 10, 450, 300, 75, 75)
        speed_x = 5
        speed_y = 3
        rocket1.get_placed()
        rocket2.get_placed()
        ball.get_placed()
    if score_l >= 7 or score_r >= 7:
        ball2.get_placed()
        ball2.rect.x += speed_x1
        ball2.rect.y += speed_y1
    if sprite.collide_rect(ball, ball2) and (score_l >= 7 or score_r >= 7):
        speed_x *= -1
        speed_x1 *= -1
        speed_y *= -1
        speed_y1 *= -1
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()