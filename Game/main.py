# from selenium import webdriver
# import tkinter
import pygame


pygame.init()

walkRight = [pygame.image.load('R1.png'),
             pygame.image.load('R2.png'),
             pygame.image.load('R3.png'),
             pygame.image.load('R4.png'),
             pygame.image.load('R5.png'),
             pygame.image.load('R6.png'),
             pygame.image.load('R7.png'),
             pygame.image.load('R8.png'),
             pygame.image.load('R9.png')]

walkLeft = [pygame.image.load('L1.png'),
            pygame.image.load('L2.png'),
            pygame.image.load('L3.png'),
            pygame.image.load('L4.png'),
            pygame.image.load('L5.png'),
            pygame.image.load('L6.png'),
            pygame.image.load('L7.png'),
            pygame.image.load('L8.png'),
            pygame.image.load('L9.png')]

bg = pygame.image.load('bg.jpg')
standing = pygame.image.load('standing.png')

clock = pygame.time.Clock()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)


HEIGHT = 480
WIDTH = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sample game ")
score = 0


class character:

    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 5
        self.isJumped = False
        self.jumpCount = 10
        self.left = True
        self.right = True
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y+7, 24, 53)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            else:
                win.blit(walkRight[0], (self.x, self.y))
        self.hitbox = (self.x + 20, self.y+7, 24, 53)

        # pygame.draw.rect(win, (225,0,0), self.hitbox,2)

    def hit(self):
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont("comicsans", 100, True)
        text = font1.render("-5", 1, (225, 0, 0))
        win.blit(text, ((WIDTH - text.get_width()) //
                        2, (HEIGHT - text.get_height())//2))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class enemy():
    walkLeft = [pygame.image.load("L1E.png"), pygame.image.load("L2E.png"), pygame.image.load("L3E.png"), pygame.image.load("L4E.png"), pygame.image.load("L5E.png"), pygame.image.load(
        "L6E.png"), pygame.image.load("L7E.png"), pygame.image.load("L8E.png"), pygame.image.load("L9E.png"), pygame.image.load("L10E.png"), pygame.image.load("L11E.png")]

    walkRight = [pygame.image.load("R1E.png"), pygame.image.load("R2E.png"), pygame.image.load("R3E.png"), pygame.image.load("R4E.png"), pygame.image.load("R5E.png"), pygame.image.load(
        "R6E.png"), pygame.image.load("R7E.png"), pygame.image.load("R8E.png"), pygame.image.load("R9E.png"), pygame.image.load("R10E.png"), pygame.image.load("R11E.png")]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x + 17, self.y, 20, 55)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount >= 33:
                self.walkCount = 0

            if self.vel < 0:
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (225, 0, 0),
                             (self.hitbox[0], self.hitbox[1]-20, 50, 10))
            pygame.draw.rect(
                win, (0, 190, 0), (self.hitbox[0], self.hitbox[1]-20, 50-(5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 20, self.y, 25, 58)
            # pygame.draw.rect(win, (225,0,0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print("HIT")


def redraw():

    win.blit(bg, (0, 0))
    text = font.render(f'Score: {score}', 1, (0, 0, 0))
    win.blit(text, (380, 12))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


# main loop
font = pygame.font.SysFont('comicsans', 32, True)
man = character(100, 410, 64, 64)
goblin = enemy(250, 410, 64, 64, 450)
bullets = []
shootLoop = 0
while True:
    clock.tick(27)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    if man.hitbox[1]  < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
        if man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2] and man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0]:
            man.hit()
            score -= 5
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for bullet in bullets:
        if bullet.y-bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2] and bullet.x + bullet.radius > goblin.hitbox[0]:
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width//2),
                                      round(man.y + man.height//2), 6, (0, 0, 0), facing))
        shootLoop = 1

    if keys[pygame.K_RIGHT] and man.x < WIDTH - man.width - 2:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False

    elif keys[pygame.K_LEFT] and man.x > 2:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not (man.isJumped):
        if keys[pygame.K_UP]:
            man.isJumped = True
            man.left = False
            man.right = False
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJumped = False
            man.jumpCount = 10

    redraw()
