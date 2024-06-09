import pygame


class Objects(pygame.Rect):
    def __init__(self, width, height, locationX, locationY, speed, image) -> None:
        super().__init__(locationX, locationY, width, height)
        self.x = locationX
        self.y = locationY
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect()
        
        
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    
    def get_x(self):
        return self.x
    

    def get_y(self):
        return self.y 