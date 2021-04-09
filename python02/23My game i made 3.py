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

    def draw(self,win):
        if self.walkCount + 1 >= 6:
            self.walkCount = 0
    
        if self.left:
            #print(walkCount//3)
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x,self.y))




isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGame():
    win.blit(bg, (0,0))
    ox.draw(win)
    pygame.display.update()

ox = player(300,410,50,50)
run = True
while run:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and ox.x > ox.vel:
        ox.x -= ox.vel
        ox.left = True
        ox.right = False
    elif keys[pygame.K_RIGHT] and ox.x < win_size - ox.width - ox.vel:
        ox.x += ox.vel
        ox.right = True
        ox.left = False
    else:
        ox.right = False
        ox.left = False
        ox.walkCount = 0
    if not(ox.isJump):
        if keys[pygame.K_SPACE]:
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