import pygame
from .Objects import Objects

class Laser(Objects):
    def __init__(self, width, height, locationX, locationY, speed, image) -> None:
        super().__init__(width, height, locationX, locationY, speed, image)

    def move(self):
        self.move_ip(0,-self.speed)
        self.y -= self.speed