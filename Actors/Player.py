import pygame
import time


class Player(pygame.Rect):
    def __init__(self, width, height, locationX, locationY, speed, image) -> None:
        super().__init__(locationX, locationY, width, height)
        self.x = locationX
        self.y = locationY
        self.width = width
        self.height = height
        self.speed = speed
        self.speed = speed

        self.shoot_timer = 0.5
        self.last_shot = 0



    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] and self.x < 800 - self.width:
            self.move_ip(self.speed,0)
            self.updateLocation(self.speed,0)
        if key[pygame.K_LEFT] and self.x  >  0:
            self.move_ip(-self.speed,0)
            self.updateLocation(-self.speed,0)

    def shoot(self):
        key = pygame.key.get_pressed()
        cur_time = time.time()
        if key[pygame.K_SPACE] and cur_time - self.last_shot > self.shoot_timer:
             self.last_shot = cur_time 
             return True
        return False

        




    def updateLocation(self, changeX, changeY):
        self.x += changeX
        self.y += changeY


    def get_x(self):
        return self.x
    

    def get_y(self):
        return self.y

    #def animate(self, direction, is_moving):


    



        
        

