import pygame
pygame.init()

win_size = 800

win = pygame.display.set_mode((win_size, win_size))

pygame.display.set_caption("Are you ready for your first game?")

x = 500
y = 500
width = 50
height = 50
vel = 5

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < win_size - width - vel:
        x += vel
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 255, 255), (x, y, width, height))
    pygame.draw.circle(win, (0, 255, 0), (x+width/4, y+height/2), 8)
    pygame.draw.circle(win, (0, 255, 0), (x+width*3/4, y+height/2), 8)
    rect = pygame.Rect(x+width/4, y+height*1.8/4, width/2, height/2)
    pygame.draw.arc(win, (0, 0, 0), rect, 3.14*1.1, 3.14*1.9, width = 1)
    
    pygame.display.update()


pygame.quit()