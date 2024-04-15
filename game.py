import pygame
import Actors.Player as Player
import os

pygame.init()

screen_width = 800
screen_height = 800



screen = pygame.display.set_mode((screen_width, screen_height))


image = pygame.image.load('Assets/Images/Running1.png')  # Replace 'your_image_file.png' with the path to your image file

# Scale the image to match the size of the rectangle
p1_image = pygame.transform.scale(image, (50, 50))  # Adjust the size as needed


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
    screen.blit(p1_image, p1)
        
    pygame.display.update()

pygame.QUIT()