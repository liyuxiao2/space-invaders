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
p1_image = load_images('Assets/Images/spaceInvadersPlane', 0, 100, 100)
p1 = Player.Player(50, 50, screen_width / 2, 800, 1, p1_image)


# Background image
bg = load_images('Assets/Images/background', 0, screen_width, screen_width)

#load laser image
l_image = load_images('Assets/Images/laser', 0, 100, 100)

# Load enemy images
enemy_image_list = load_images('Assets/Images/badguy', 5, 50, 50)

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

    
    if score == 500:
        game_over = font.render("GAME OVER (click spacebar to quit)" , 1, (255,255,255)) # Arguments are: text, anti-aliasing, color
        screen.blit(game_over, (screen_width/2,screen_height/2))
