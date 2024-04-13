import pygame

class Player(pygame.Rect):
    def __init__(self, width, height, locationX, locationY, speed) -> None:
        super().__init__(locationX, locationY, width, height)
        self.locationX = locationX
        self.locationY = locationY
        self.width = width
        self.height = height
        self.speed = speed



    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d] and self.locationX < 800 - self.width:
            self.move_ip(self.speed,0)
            self.updateLocation(self.speed,0)
        if key[pygame.K_a] and self.locationX  >  0:
            self.move_ip(-self.speed,0)
            self.updateLocation(-self.speed,0)
        if key[pygame.K_w] and self.locationY > 0:
            self.move_ip(0,-self.speed)
            self.updateLocation(0,-self.speed)
        if key[pygame.K_s] and self.locationY  < 800-self.height:
            self.move_ip(0,self.speed)
            self.updateLocation(0,self.speed)
    

    def updateLocation(self, changeX, changeY):
        self.locationX += changeX
        self.locationY += changeY
    

