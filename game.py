import pygame
import Actors.Player as Player
import os

pygame.init()

screen_width = 800
screen_height = 800




screen = pygame.display.set_mode((screen_width, screen_height))


#set values for player
walkingRight = [pygame.image.load('Assets/Images/Running1.png'), pygame.image.load('Assets/Images/Running2.png'), pygame.image.load('Assets/Images/Running3.png'), pygame.image.load('Assets/Images/Running4.png'), pygame.image.load('Assets/Images/Running5.png') ]

char = pygame.image.load('Assets/Images/Running1.png')  # Replace 'your_image_file.png' with the path to your image file

# Scale the image to match the size of the rectangle
p1_image = pygame.transform.scale(char, (50, 50))  # Adjust the size as needed

p1 = Player.Player(50,50,screen_width/2,screen_height/2, 5)

run = True




#background image
bgimage = pygame.image.load('Assets/Images/background.png')

bg = pygame.transform.scale(bgimage, (screen_width, screen_height))




while(run):
    screen.fill([255, 255, 255])
    screen.blit(bg, (0,0))

    #handles movement
    p1.move()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False





    #creates playe
    screen.blit(p1_image, p1)
        
    pygame.display.update()

pygame.QUIT()





