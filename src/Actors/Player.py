import pygame
import time
from .functions.collision import check_collision  # Use absolute import

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

laser_path = '/Users/liyuxiao/Documents/CS/project-game/src/Assets/Audio/laser.mp3'
laser_sound = pygame.mixer.Sound(laser_path)


class Player(pygame.Rect):
    def __init__(self, width, height, locationX, locationY, speed, image) -> None:
        super().__init__(locationX, locationY, width, height)
        self.x = locationX
        self.y = locationY
        self.width = width
        self.height = height
        self.speed = speed
        self.shoot_timer = 0.5
        self.last_shot = 0
        self.lives = 3
        self.alive = True



    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] and self.x < 1000 - self.width:
            self.move_ip(self.speed*0.5,0)
            self.updateLocation(self.speed,0)
        if key[pygame.K_LEFT] and self.x  >  0:
            self.move_ip(-self.speed,0)
            self.updateLocation(-self.speed*0.5,0)



    def shoot(self):
        key = pygame.key.get_pressed()
        cur_time = time.time()
        if key[pygame.K_SPACE] and cur_time - self.last_shot > self.shoot_timer:
            laser_sound.play()
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
    
    
    def get_lives(self):
        return self.lives
    
    
    def die(self, laser):
        if check_collision(self, laser) and self.alive:  # Check collision and alive state
            if(self.lives <= 0):
                return True  # Mark enemy as dead
            else:
                self.lives -= 1
        return False  # Enemy is not hit by this laser


    



        
        

