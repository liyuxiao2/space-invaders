import pygame
from .Objects import Objects
from .functions.collision import check_collision  # Use absolute import
import time


pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

death_path = "/Users/liyuxiao/Documents/CS/project-game/src/Assets/Audio/death.wav"
death_sound = pygame.mixer.Sound(death_path)

death_image = "/Users/liyuxiao/Documents/CS/project-game/src/Assets/Images/explosion.png"
class Enemy(Objects):
    def __init__(self, width, height, locationX, locationY, speed, image, points) -> None:
        super().__init__(width, height, locationX, locationY, speed, image)
        self.points = points
        self.move_timer = 1
        self.last_move = 0
        self.alive = True  # Add a flag to track enemy's alive state
        self.death_timer = None  # Timer for delay between enemy and explosion image
        self.explosion_image = pygame.image.load(death_image)
        self.explosion = pygame.transform.scale(self.explosion_image, (width, height))

    def move(self):
        cur_time = time.time()
        if cur_time - self.last_move > self.move_timer:
            self.last_move = cur_time 
            if self.x < 1100 - self.width:  # Check if enemy is within the screen width
                self.move_ip(50, 0)  # Move enemy to the right
            else:
                # Calculate the exact position on the left side of the screen
                new_x = -self.x  # Set x-coordinate to the left edge of the screen
                new_y = 100  # Move enemy down by 100 units (adjust as needed)
                self.move_ip(new_x, new_y)  # Move enemy to the calculated position

    def die(self, laser):
        if check_collision(self, laser) and self.alive:  # Check collision and alive state
            death_sound.play()
            self.alive = False  # Mark enemy as dead
            self.death_timer = time.time()  # Start death timer for removal
            self.image = death_image  # Update image to explosion
            return True  # Indicate enemy is hit (for removal)
        return False  # Enemy is not hit by this laser

    
    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, (self.x, self.y))  # Draw enemy image if alive
        else:
            current_time = time.time()
            if current_time - self.death_timer <= 0.5:  # Check if 0.5 seconds have passed
                screen.blit(self.explosion, (self.x, self.y))  # Draw explosion image during delay

    def get_points(self):
        return self.points

    

    def colliderect(self, other):
         # Check for collision between this object and another object
        if ((self.x < other.x + other.width and
            self.x + self.width > other.x) or
            (self.y < other.y + other.height and
            self.y + self.height > other.y)):
            return True
        else:
            return False
        
        
    
