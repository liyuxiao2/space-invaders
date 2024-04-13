import pygame
import Player

pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))


p1 = Player.Player(50,50,400,400, 10)

run = True

while(run):
    screen.fill((0,0,0)) 
    pygame.draw.rect(screen, (255,0,0), p1)

    p1.move()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()

pygame.QUIT()