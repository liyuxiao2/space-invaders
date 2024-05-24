import pygame
import Actors.Player as Player
import Actors.Enemy as Enemy
import Actors.Laser as Laser

pygame.init()


screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

char = pygame.image.load('Assets/Images/spaceInvadersPlane.png')
p1_image = pygame.transform.scale(char, (100, 100))
p1 = Player.Player(50, 50, screen_width / 2, 600, 2, char)

# Background image
bgimage = pygame.image.load('Assets/Images/background.png')
bg = pygame.transform.scale(bgimage, (screen_width, screen_height))

#Laser Image
laserImage = pygame.image.load('Assets/Images/laser.png')
l_image = pygame.transform.scale(laserImage, (100, 100))

# Enemy image
enemy_image1 = pygame.image.load('Assets/Images/badguy.png')

eimage1 = pygame.transform.scale(enemy_image1, (50, 50))


# Create enemies
enemies = []

#create lasers

lasers = []


for i in range(4):
    for j in range(20):
        enemy = Enemy.Enemy(50, 50, 0+j*50, 0+i*100, 0, eimage1)
        enemies.append(enemy)

run = True
while run:
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # Handle player movement
    p1.move()

    #check if lasers are shot
    if(p1.shoot() == True):
        laser = Laser.Laser(50, 50, p1.get_x()+1, p1.get_y()-60, 2, l_image)
        lasers.append(laser)

    # Move and draw lasers
    for laser in lasers:
        laser.move()
        screen.blit(laser.image, (laser.x, laser.y))

    # draw enemies
    for enemy in enemies:
        screen.blit(enemy.image, (enemy.x, enemy.y) )  # Draw enemy


    # Check if enemies are hit and remove them
    enemies_to_remove = []  # List to store enemies to remove

    for enemy in enemies:
        if enemy.die(Laser):
            print("im dead!")
            enemies_to_remove.append(enemy)

    # Remove the hit enemies from the main enemies list
    for enemy in enemies_to_remove:
        enemies.remove(enemy)


    # Draw player
    screen.blit(p1_image, p1)

    pygame.display.update()

    # Quit Pygame when SPACE key is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_y]:
        pygame.quit()
            
