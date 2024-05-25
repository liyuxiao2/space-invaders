import pygame
import Actors.Player as Player
import Actors.Enemy as Enemy
import Actors.Laser as Laser
from Actors.functions.utilityfunctions import load_images, handle_collisions, animation

pygame.init()

# Initialize the game
screen_width = 1100
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

# Load character
char = pygame.image.load('Assets/Images/spaceInvadersPlane.png')
p1_image = pygame.transform.scale(char, (100, 100))
p1 = Player.Player(50, 50, screen_width / 2, 800, 1, p1_image)

# Background image
bgimage = pygame.image.load('Assets/Images/background.png')
bg = pygame.transform.scale(bgimage, (screen_width, screen_height))

# Laser image
laser_image = pygame.image.load('Assets/Images/laser.png')
l_image = pygame.transform.scale(laser_image, (100, 100))

# Load enemy images
enemy_image_list = load_images('Assets/Images/badguy', 5)

# Initialize lists
enemies = []
lasers = []
run = True

# Load all enemies onto the map
for i in range(5):
    for j in range(10):
        enemy = Enemy.Enemy(100, 100, 0 + j * 100, 100 + i * 100, 0, enemy_image_list[i])
        enemies.append(enemy)



#intialize scorebar
score = 0

font = pygame.font.SysFont("comicsans", 30, True)




# Main game loop
while run:
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))

    text = font.render("Score: " + str(score), 1, (255,255,255)) # Arguments are: text, anti-aliasing, color
    screen.blit(text, (900,0))

    lasers_to_remove = []
    enemies_to_remove = []

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Handle player movement
    p1.move()

    # Check if lasers are shot
    if p1.shoot():
        laser = Laser.Laser(25, 25, p1.get_x() + 1, p1.get_y() - 60, 1, l_image)
        lasers.append(laser)

    # Move and draw lasers
    for laser in lasers:
        laser.move()
        screen.blit(laser.image, (laser.x, laser.y))

    # Draw enemies
    for enemy in enemies:
        enemy.move()
        screen.blit(enemy.image, (enemy.x, enemy.y))

    # Check for collisions
    handle_collisions(enemies, lasers, enemies_to_remove, lasers_to_remove)

    # Remove collided enemies and lasers
    for enemy in enemies_to_remove:
        score += 10
        enemies.remove(enemy)
    for laser in lasers_to_remove:
        lasers.remove(laser)

    # Draw player
    screen.blit(p1_image, (p1.x, p1.y))

    pygame.display.update()

    # Quit Pygame when SPACE key is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_y]:
        pygame.quit()
