# 6 enemies at 
# https://www.youtube.com/watch?v=vc1pJ8XdZa0&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&index=6
import pygame
pygame.init()

win_size = 800

win = pygame.display.set_mode((win_size, win_size))

pygame.display.set_caption("Are you ready for your first game?")

walkLeft = [pygame.image.load('./python02/ox02.png'),
            pygame.image.load('./python02/ox02.png'),
            pygame.image.load('./python02/ox02.png')]
walkRight = [pygame.image.load('./python02/ox01.png'),
            pygame.image.load('./python02/ox01.png'),
            pygame.image.load('./python02/ox01.png')]
bg = pygame.image.load('./python02/oxbg.jpeg')
char = pygame.image.load('./python02/ox01.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

    def draw(self,win):
        if self.walkCount + 1 >= 6:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                #print(walkCount//3)
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
class enemy(object):
    walkRight = [pygame.image.load('./python02/cat02.png')]
    walkLeft = [pygame.image.load('./python02/cat03.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3

    def draw(self, win):
        self.move()
        if self.walkCount + 1 <= 33:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
            self.walkCount += 1


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
        




class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)



isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
horns = []
def redrawGame():
    win.blit(bg, (0,0))
    ox.draw(win)
    cat.draw(win)
    for horn in horns:
        horn.draw(win)

    pygame.display.update()

ox = player(300, 410, 50, 50)
cat = enemy(200, 410, 50, 50, 790)

run = True
while run:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for horn in horns:
        if horn.x < 500 and horn.x > 0:
            horn.x += horn.vel
        else:
            horns.pop(horns.index(horn))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if ox.left:
            facing = -1
        else:
            facing = 1
        if len(horns) < 5:
            horns.append(projectile(round(ox.x + ox.width), round(ox.y + ox.height//2), 6, (255,255,255), facing))

    if keys[pygame.K_LEFT] and ox.x > ox.vel:
        ox.x -= ox.vel
        ox.left = True
        ox.right = False
        ox.standing = False

    elif keys[pygame.K_RIGHT] and ox.x < win_size - ox.width - ox.vel:
        ox.x += ox.vel
        ox.right = True
        ox.left = False
        ox.standing = False
    else:
        ox.standing = True
        ox.walkCount = 0
    if not(ox.isJump):
        if keys[pygame.K_UP]:
            ox.isJump = True
            ox.right = False
            ox.left = False
            ox.walkCount = 0

    else:
        if ox.jumpCount >= -10:
            neg = 1
            if ox.jumpCount < 0:
                neg = -1
            ox.y -= (ox.jumpCount ** 2) * 0.5 * neg
            ox.jumpCount -= 1
        else:
            ox.isJump = False
            ox.jumpCount = 10
    
    pygame.display.update()

    redrawGame()

pygame.quit()