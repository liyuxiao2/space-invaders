import pygame
from .Objects import Objects
from .functions.collision import check_collision  # Use absolute import
import time


class Enemy(Objects):
    def __init__(self, width, height, locationX, locationY, speed, image) -> None:
        super().__init__(width, height, locationX, locationY, speed, image)
        self.image = image

        self.move_timer = 1
        self.last_move = 0

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
        if check_collision(self, laser):  # Use check_collision function
            return True  # Enemy is hit and should be removed
        return False  # Enemy is not hit by this lase

    

    def colliderect(self, other):
         # Check for collision between this object and another object
        if ((self.x < other.x + other.width and
            self.x + self.width > other.x) or
            (self.y < other.y + other.height and
            self.y + self.height > other.y)):
            return True
        else:
            return False

