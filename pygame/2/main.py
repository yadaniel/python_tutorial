#!/cygdrive/c/Python39/python

import pygame, random
import sys, time
import math

# general settings
w,h=1200,600
snd_file = "laser_shot.mp3"
jmp_file = "jump.mp3"

pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.key.set_repeat(1,5)
# pygame.key.set_repeat(1,10)
pygame.display.set_caption("Jana Spiel")
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((w,h))
screen.fill((255,255,0))
clock = pygame.time.Clock()
random.seed(time.time())

# points = [(25, 0), (50, 25), (25, 50), (0, 25)]
# pygame.draw.polygon(screen, (255,255,255), points)

class ball(object):
    def __init__(self, screen, pos, r, p1, p2):
        self.screen = screen
        self.r = r
        self.pos = pos
        self.phi = float(random.randint(0,360))
        self.speed = random.randint(1,10)
        self.c = self.speed*math.e**(1j*self.phi/360.0*2*math.pi)
        self.color = pygame.Color(255,255,255)
        self.it = pygame.draw.circle(self.screen, self.color, self.pos, self.r)
    def tick(self,upper, lower, left, right):
        #
        collide = False
        re,im = self.c.real, self.c.imag
        for r in upper:
            if self.it.colliderect(r):
                self.c = re - im*1j
                collide = True
        for r in lower:
            if self.it.colliderect(r):
                self.c = re - im*1j
                collide = True
        for r in left:
            if self.it.colliderect(r):
                self.c = -re + im*1j
                collide = True
                p2.count += 1
        for r in right:
            if self.it.colliderect(r):
                self.c = -re + im*1j
                collide = True
                p1.count += 1
        for r in [p1.r, p2.r]:
            if self.it.colliderect(r):
                self.c = -re + im*1j
                pygame.mixer.music.load(jmp_file)
                pygame.mixer.music.play()
        #
        if collide:
            # x,y = self.pos
            # x -= self.c.real
            # y -= self.c.imag
            # self.pos = (x,y)
            # self.phi = float(random.randint(0,360))
            # self.speed = random.randint(1,10)
            # self.c = self.speed*math.e**(1j*self.phi/360.0*2*math.pi)
            self.color = pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            pygame.mixer.music.load(snd_file)
            pygame.mixer.music.play()

        #
        # self.c *= 1.01
        self.c *= 1.0
        x,y = self.pos
        x += self.c.real
        y += self.c.imag
        self.pos = (x,y)
        return self.pos

    def draw(self):
        self.it = pygame.draw.circle(self.screen, self.color, self.pos, self.r)

class player(object):
    def __init__(self, screen, id, up_key, down_key):
        self.count = 0
        self.id = id
        self.screen = screen
        self.up_key = up_key
        self.down_key = down_key
        if id == 1:
            self.pos = (40,h//2)
            self.color = pygame.Color(255,255,255)
        else:
            self.pos = (w-60,h//2)
            self.color = pygame.Color(255,0,255)
        self.dim = (10,50)
        self.r = pygame.draw.rect(self.screen, self.color, (*self.pos, *self.dim))
    # def tick(self,e):
    def tick(self, keys):

        if keys[self.up_key]:
            print(f"player {self.id}: left")
            x,y = self.pos
            if y + 70 < h:
                y += 10
            self.pos = (x,y)
        elif keys[self.down_key]:
            print(f"player {self.id}: right")
            x,y = self.pos
            if y - 20 > 0:
                y -= 10
            self.pos = (x,y)

        # if e.type == pygame.KEYDOWN:
        #     if e.key == self.up_key:
        #         print(f"player {self.id}: left")
        #         x,y = self.pos
        #         if y + 70 < h:
        #             y += 5
        #         self.pos = (x,y)
        #     elif e.key == self.down_key:
        #         print(f"player {self.id}: right")
        #         x,y = self.pos
        #         if y - 20 > 0:
        #             y -= 5
        #         self.pos = (x,y)

    def draw(self):
        self.r = pygame.draw.rect(self.screen, self.color, (*self.pos, *self.dim))

p1 = player(screen, 1, up_key = pygame.K_DOWN, down_key = pygame.K_UP)
# p2 = player(screen, 2, up_key = pygame.K_LEFT, down_key = pygame.K_RIGHT)
p2 = player(screen, 2, up_key = pygame.K_KP_PLUS, down_key = pygame.K_KP_MINUS)
b = ball(screen, pos=(w//2, h//2), r=10, p1=p1, p2=p2)

while True:
    keys = pygame.key.get_pressed()
    # print(keys)

    if keys[pygame.K_ESCAPE]:
        sys.exit()

    # for e in pygame.event.get():
    #     if e.type == pygame.QUIT:
    #         sys.exit()

        # if e.type == pygame.KEYDOWN:
        #     if e.key == pygame.K_LEFT:
        #         print("left")
        #     elif e.key == pygame.K_RIGHT:
        #         print("right")
        #     elif e.key == pygame.K_UP:
        #         print("up")
        #     elif e.key == pygame.K_DOWN:
        #         print("down")
        #     elif e.key == pygame.K_SPACE:
        #         pass
        #     elif e.key == pygame.K_ESCAPE:
        #         sys.exit()
        #     else:
        #         pass
    
    clock.tick(60)
    screen.fill((0,0,0))
    # screen.fill([random.randint(0,255) for i in range(3)])
    # pygame.draw.circle(screen, (0,255,255), (x,y), r)

    # upper border
    upper1 = pygame.draw.rect(screen, (255,255,255), (10,10,w//2-10,10))
    upper2 = pygame.draw.rect(screen, (255,0,255), (w//2+10,10,w//2-20,10))

    # lower border
    lower1 = pygame.draw.rect(screen, (255,255,255), (10,h-20,w//2-10,10))
    lower2 = pygame.draw.rect(screen, (255,0,255), (w//2+10,h-20,w//2-20,10))

    # left border
    left1 = pygame.draw.rect(screen, (255,255,255), (10,20,10,h-40))

    # right
    right1 = pygame.draw.rect(screen, (255,0,255), (w-20,20,10,h-40))

    b.tick([upper1, upper2], [lower1, lower2], [left1], [right1])
    b.draw()

    # p1.tick(e)
    # p2.tick(e)
    p1.tick(keys)
    p2.tick(keys)
    p1.draw()
    p2.draw()
    player_count = myfont.render(f'{p1.count}:{p2.count}', False, (255, 255, 0))
    screen.blit(player_count,(w//2-20,30))

    pygame.display.update()
    pygame.event.pump()

