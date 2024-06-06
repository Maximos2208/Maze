import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1820,980))
done = False

x=60
y=60
x1=120
y1=60

clock = pygame.time.Clock()
#timer1 = time.time()
#timer2 = time.time()
stopwatch1 = time.time()
stopwatch2 = time.time()
timer1Updated = 0
timer2Updated = 0



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill((0,0,0))
    Font = pygame.font.SysFont("comicsansms", 70, True, True)
    Title = Font.render("Maze Finder",True,(255,255,255))
    screen.blit(Title, (650,450))



    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_w]: y=y-12
    if pressed[pygame.K_d]: x=x+12
    if pressed[pygame.K_s]: y=y+12
    if pressed[pygame.K_a]: x=x-12

    if pressed[pygame.K_i]: y1 = y1 - 12
    if pressed[pygame.K_l]: x1 = x1 + 12
    if pressed[pygame.K_k]: y1 = y1 + 12
    if pressed[pygame.K_j]: x1 = x1 - 12
    player1 = pygame.draw.rect(screen, (200,129,0), pygame.Rect(x, y, 50, 50))
    player2 = pygame.draw.rect(screen, (76,153 ,0), pygame.Rect(x1, y1, 50, 50))


    wall1 = pygame.draw.rect(screen, (200,129,0), pygame.Rect(0,0, 1800,50))
    wall2 = pygame.draw.rect(screen, (200,129,0), pygame.Rect(0, 0, 50, 980))
    wall3 = pygame.draw.rect(screen, (200,129,0), pygame.Rect(0, 930, 1810, 50))
    wall4 = pygame.draw.rect(screen, (200,129,0), pygame.Rect(1770, 0, 50, 980))

    wall5 = pygame.draw.rect(screen, (200, 129, 0), pygame.Rect(200,50, 50, 700))
    wall6 = pygame.draw.rect(screen, (200, 129, 0), pygame.Rect(400,650, 50, 750))
    wall7 = pygame.draw.rect(screen, (200, 129, 0), pygame.Rect(600,50, 50, 800))
    wall8 = pygame.draw.rect(screen, (200, 129, 0), pygame.Rect(825,500, 50,750))
    wall9 = pygame.draw.rect(screen, (200, 129, 0), pygame.Rect(1000,50, 50,750))

    final = pygame.draw.rect(screen, (200, 129, 0), pygame.Rect(1500, 50, 70,70))

    if player1.colliderect(wall1) or player1.colliderect(wall2) or player1.colliderect(wall3) or player1.colliderect(wall4) or player1.colliderect(wall5) or player1.colliderect(wall6) or player1.colliderect(wall7) or player1.colliderect(wall8) or player1.colliderect(wall9):
        if pressed[pygame.K_w]: y=y+12
        if pressed[pygame.K_s]: y=y-12
        if pressed[pygame.K_a]: x=x+12
        if pressed[pygame.K_d]: x=x-12
    if player2.colliderect(wall1) or player2.colliderect(wall2) or player2.colliderect( wall3) or player2.colliderect(wall4) or player2.colliderect(wall5) or player2.colliderect( wall6) or player2.colliderect(wall7) or player2.colliderect(wall8) or player2.colliderect(wall9):


        if pressed[pygame.K_i]: y1 = y1 + 12
        if pressed[pygame.K_l]: x1 = x1 - 12
        if pressed[pygame.K_k]: y1 = y1 + 12
        if pressed[pygame.K_j]: x1 = x1 - 12


    if player1.colliderect(final):
        x = 60
        y = 60
        timer1 = time.time()
        timer1Updated = round(timer1 - stopwatch1,2)
        stopwatch1 = time.time()

    Font1 = pygame.font.SysFont("comicsansms",20, True, True)
    Time1 = Font1.render("Time for player 1: " + str(timer1Updated),True,(200, 129 , 0))
    screen.blit(Time1, (1100,600))



    if player2.colliderect(final):
        x = 120
        y = 60
        timer2 = time.time()
        timer2Updated = round(timer2 - stopwatch2,2)
        stopwatch2 = time.time()

    Font2 = pygame.font.SysFont("comicsansms",20, True, True)
    Time2 = Font2.render("Time for player 2: " + str(timer2Updated),True,(76, 153, 0))
    screen.blit(Time2, (1050,650))

    pygame.display.flip()
    clock.tick(60)