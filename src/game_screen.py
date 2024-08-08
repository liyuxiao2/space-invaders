import pygame
import Actors.Player as Player
import Actors.Enemy as Enemy
import Actors.Laser as Laser
from Actors.functions.utilityfunctions import load_images, handle_collisions, handle_player_collisions, transition_effect
import time

class GameScreen:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.font = pygame.font.SysFont("Tahoma", 30, True)
        
        # Load character
        self.p1_image = load_images('/Users/liyuxiao/Documents/CS/project-game/src/Assets/Images/spaceInvadersPlane', 0, 100, 100)
        self.p1 = Player.Player(50, 50, screen_width / 2, 800, 2, self.p1_image)

        # Background image
        self.bg = load_images('/Users/liyuxiao/Documents/CS/project-game/src/Assets/Images/background', 0, screen_width, screen_width)

        # Load laser image
        self.l_image = load_images('/Users/liyuxiao/Documents/CS/project-game/src/Assets/Images/laser', 0, 100, 100)
        self.l_e_image = load_images('/Users/liyuxiao/Documents/CS/project-game/src/Assets/Images/enemy_laser', 0, 50,50)

        # Load enemy images
        self.enemy_image_list = load_images('/Users/liyuxiao/Documents/CS/project-game/src/Assets/Images/badguy', 5, 50, 50)

        # Initialize lists
        self.enemies = []
        self.lasers = []
        self.enemy_lasers = []
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
            
            lives = self.font.render("Lives " + str(int(self.hitpoints)),1 , (255,255,255))
            self.screen.blit(lives, (0,0))

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
                
            # Draw enemies
            for enemy in self.enemies:
                enemy.move()
                enemy.draw(self.screen)  # Use draw method to handle alive and dead states
                if enemy.shoot():
                    laser = Laser.Laser(25, 25, enemy.get_x() + 1, enemy.get_y() + 60, 1, self.l_e_image)
                    self.enemy_lasers.append(laser)
                
            # Move and draw lasers
            for laser in self.lasers:
                laser.move(-1)
                self.screen.blit(laser.image, (laser.x, laser.y))
                    
            for laser in self.enemy_lasers:
                laser.move(+1)  # Move enemy laser to the right
                self.screen.blit(laser.image, (laser.x, laser.y))
                    
            # Check for collisions
            self.score += handle_collisions(self.enemies, self.lasers, enemies_to_remove, lasers_to_remove)
            self.hitpoints -= handle_player_collisions(self.p1, self.enemy_lasers, lasers_to_remove)

            # Remove collided enemies and lasers safely
            self.lasers = [laser for laser in self.lasers if laser not in lasers_to_remove]
            self.enemy_lasers = [laser for laser in self.enemy_lasers if laser not in lasers_to_remove]
            

            # Draw player
            self.screen.blit(self.p1_image, (self.p1.x, self.p1.y))

            # Check for game over condition
            if self.score == 1500 or self.hitpoints == 0:
                game_over = self.font.render("GAME OVER (click spacebar to quit)", 1, (255, 0, 51))  # Arguments are: text, anti-aliasing, color
                self.screen.blit(game_over, (300, 300))
                pygame.display.update()
                pygame.time.wait(2000)  # Wait for 2 seconds
                transition_effect(self.screen, self.screen_width, self.screen_height, self.return_to_home_screen)
                

            pygame.display.update()

        pygame.quit()
        
        
    def return_to_home_screen(self):
        # Reset game state here
        self.score = 0
        self.hitpoints = 3
        self.run = True
        self.lasers = []
        self.enemy_lasers = []
        self.enemies = []
        for i in range(5):
            for j in range(10):
                enemy = Enemy.Enemy(100, 100, 0 + j * 100, 100 + i * 100, 0, self.enemy_image_list[i], 50 - (i) * 10)
                self.enemies.append(enemy)

        # Optionally, clear any other game-specific attributes

        # Return to home screen
        self.home_screen()


# Usage
def main():
    game = GameScreen(1200, 800)
    if game.home_screen():
        game.run_game()

if __name__ == "__main__":
    main()
