from pygame import *
win = display.set_mode((900, 600))
display.set_caption('Не_Пифики_Пафики')
bg = transform.scale(image.load('backg.png'), (900,600))
game = True
finish = False
speed_x = 5
speed_y = 3
clock = time.Clock()
FPS = 60

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
    def __init__(self, pic, speed, x, y, size_x, size_y, p_num):
        super().__init__(pic, speed, x, y, size_x, size_y)
        self.num = p_num
    def get_moving(self):
        keys = key.get_pressed()
        if self.num == 1 and keys[K_w] and self.rect.y >= 20:
            self.rect.y -= self.speed
        if self.num == 1 and keys[K_s] and self.rect.y <= 430:
            self.rect.y += self.speed
        if self.num == 2 and keys[K_UP] and self.rect.y >= 20:
            self.rect.y -= self.speed
        if self.num == 2 and keys[K_DOWN] and self.rect.y <= 430:
            self.rect.y += self.speed

rocket1 = Player('rock1.png', 10, 50, 100, 50, 150, 1)
rocket2 = Player('rock2.png', 10, 800, 400, 50, 150, 2)
ball = GameSprite('balls.png', 10, 450, 300, 75, 75,)
while game:
    clock.tick(FPS)
    win.blit(bg, (0,0))
    rocket1.get_placed()
    rocket2.get_placed()
    ball.get_placed()
    if finish != True:
        rocket1.get_moving()
        rocket2.get_moving()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y <= 25 or ball.rect.y >= 650:
        speed_y *= -1
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()