import pygame
from .Objects import Objects
from .Laser import Laser

class Enemy(Objects):
    def __init__(self, width, height, locationX, locationY, speed, image) -> None:
        super().__init__(width, height, locationX, locationY, speed, image)
        self.image = image

    def die(self, other):
        if isinstance(other, Laser):  # Check if 'other' is an instance of Laser
            if self.colliderect(other):  # Check for collision between enemy and laser
                return True  # Enemy is hit and should be removed
        return False  # Enemy is not hit by the laser
    

    def colliderect(self, other):
         # Check for collision between this object and another object
        if ((self.x < other.x + other.width and
            self.x + self.width > other.x) or
            (self.y < other.y + other.height and
            self.y + self.height > other.y)):
            return True
        else:
            return False

