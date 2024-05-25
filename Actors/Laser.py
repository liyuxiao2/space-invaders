import pygame
from .Objects import Objects
from .functions.collision import check_collision  # Use absolute import

class Laser(Objects):
    def __init__(self, width, height, locationX, locationY, speed, image) -> None:
        super().__init__(width, height, locationX, locationY, speed, image)

    def move(self):
        self.move_ip(0,-self.speed)
        self.y -= self.speed
        self.move_ip(0, -self.speed)
        self.y -= self.speed

    def die(self, enemy):  # Change the parameter to a single enemy
        if check_collision(self, enemy):  # Use check_collision function
            return True  # Enemy is hit and should be removed
        return False  # Enemy is not hit by this lase