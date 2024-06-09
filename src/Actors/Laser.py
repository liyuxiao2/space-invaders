import pygame
from .Objects import Objects
from .Player import Player
from .functions.collision import check_collision  # Use absolute import
from typing import Union

class Laser(Objects):
    def __init__(self, width, height, locationX, locationY, speed, image) -> None:
        super().__init__(width, height, locationX, locationY, speed, image)

    def move(self, direction):
        self.move_ip(0,direction*self.speed)
        self.y += direction*self.speed

    def die(self, obj: Union[Objects, Player]) -> bool:  # Use Union type hint
        if isinstance(obj, Objects):  # Check if object inherits from Objects
            return check_collision(self, obj)
        else:
            return False