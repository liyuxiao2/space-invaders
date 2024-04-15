import pygame
import Actors.Player as Player

pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))


p1 = Player.Player(50,50,screen_width/2,screen_height/2, 15)

run = True

while(run):
    

    #handles movement
    p1.move()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




    #resets screen
    screen.fill((0,0,0)) 

    #creates playe
    pygame.draw.rect(screen, (255,0,0), p1)
        
    pygame.display.update()

pygame.QUIT()