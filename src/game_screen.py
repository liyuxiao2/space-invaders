import pygame
import Actors.Player as Player
import Actors.Enemy as Enemy
import Actors.Laser as Laser
from Actors.functions.utilityfunctions import load_images, handle_collisions, animation
import time

class GameScreen:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.font = pygame.font.SysFont("comicsans", 30, True)
        
        # Load character
        self.p1_image = load_images('/Users/liyuxiao/Documents/CS/project-game/src/Assets/Images/spaceInvadersPlane', 0, 100, 100)
        self.p1 = Player.Player(50, 50, screen_width / 2, 800, 1, self.p1_image)

        # Background image
        self.bg = load_images('/Users/liyuxiao/Documents/CS/project-game/src/Assets/Images/background', 0, screen_width, screen_width)

        # Load laser image
        self.l_image = load_images('/Users/liyuxiao/Documents/CS/project-game/src/Assets/Images/laser', 0, 100, 100)

        # Load enemy images
        self.enemy_image_list = load_images('/Users/liyuxiao/Documents/CS/project-game/src/Assets/Images/badguy', 5, 50, 50)

        # Initialize lists
        self.enemies = []
        self.lasers = []

        # Load all enemies onto the map
        for i in range(5):
            for j in range(10):
                enemy = Enemy.Enemy(100, 100, 0 + j * 100, 100 + i * 100, 0, self.enemy_image_list[i], 50 - (i) * 10)
                self.enemies.append(enemy)

        # Initialize score
        self.score = 0
        self.hitpoints = 3
        self.run = True

    def home_screen(self):
        while True:
            self.screen.fill((0, 0, 0))
            title_text = self.font.render("Welcome to Space Invaders!", True, (255, 255, 255))
            start_text = self.font.render("Press SPACE to Start", True, (255, 255, 255))
            self.screen.blit(title_text, (self.screen_width / 2 - title_text.get_width() / 2, 100))
            self.screen.blit(self.enemy_image_list[0],(self.screen_width / 2, 200))
            self.screen.blit(self.enemy_image_list[1],(self.screen_width / 2, 300))
            self.screen.blit(self.enemy_image_list[2],(self.screen_width / 2, 400))
            self.screen.blit(self.enemy_image_list[3],(self.screen_width / 2, 500))
            self.screen.blit(self.enemy_image_list[4],(self.screen_width / 2, 600))
            
            
            self.screen.blit(start_text, (self.screen_width / 2 - start_text.get_width() / 2, 700))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return True

    def run_game(self):
        while self.run:
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.bg, (0, 0))

            # Update score text
            text = self.font.render("Score: " + str(self.score), 1, (255, 255, 255))  # Arguments are: text, anti-aliasing, color
            self.screen.blit(text, (900, 0))

            lasers_to_remove = []
            enemies_to_remove = []

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            # Handle player movement
            self.p1.move()

            # Check if lasers are shot
            if self.p1.shoot():
                laser = Laser.Laser(25, 25, self.p1.get_x() + 1, self.p1.get_y() - 60, 1, self.l_image)
                self.lasers.append(laser)

            # Move and draw lasers
            for laser in self.lasers:
                laser.move()
                self.screen.blit(laser.image, (laser.x, laser.y))
                if(laser.die(self.p1)):
                    self.p1.die()

            # Draw enemies
            for enemy in self.enemies:
                enemy.move()
                enemy.draw(self.screen)  # Use draw method to handle alive and dead states
                
                
                
            
            # Check for collisions
            self.score += handle_collisions(self.enemies, self.lasers, enemies_to_remove, lasers_to_remove)

            # Update score and remove collided enemies and lasers

            for laser in lasers_to_remove:
                self.lasers.remove(laser)

            # Draw player
            self.screen.blit(self.p1_image, (self.p1.x, self.p1.y))

            # Check for game over condition
            if self.score >= 500:
                game_over = self.font.render("GAME OVER (click spacebar to quit)", 1, (255, 255, 255))  # Arguments are: text, anti-aliasing, color
                self.screen.blit(game_over, (self.screen_width / 2, self.screen_height / 2))
                pygame.display.update()
                pygame.time.wait(2000)  # Wait for 2 seconds
                self.run = False

            pygame.display.update()

        pygame.quit()

# Usage
def main():
    game = GameScreen(1200, 800)
    if game.home_screen():
        game.run_game()

if __name__ == "__main__":
    main()
