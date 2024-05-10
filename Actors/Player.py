import pygame

class Player(pygame.Rect):
    def __init__(self, width, height, locationX, locationY, speed) -> None:
        super().__init__(locationX, locationY, width, height)
        self.locationX = locationX
        self.locationY = locationY
        self.width = width
        self.height = height
        self.speed = speed
        self.speed = speed

        self.vel_y = 0



    def move(self):

        key = pygame.key.get_pressed()
        if key[pygame.K_d] and self.locationX < 800 - self.width:
            self.move_ip(self.speed,0)
            self.updateLocation(self.speed,0)
        if key[pygame.K_a] and self.locationX  >  0:
            self.move_ip(-self.speed,0)
            self.updateLocation(-self.speed,0)
        if key[pygame.K_SPACE] and self.locationY > 0:
            self.move_ip(0,-self.speed)
            self.updateLocation(0,-self.speed)
        if key[pygame.K_s] and self.locationY  < 800-self.height:
            self.move_ip(0,self.speed)
            self.updateLocation(0,self.speed)

        

        


       



        # Check if the player hits the ground
        if self.locationY >= 800 - self.height:
            self.locationY = 800 - self.height
            self.vel_y = 0  
        else:
            # Apply gravity
            self.vel_y += 0.5
            self.move_ip(0,self.vel_y)
            self.updateLocation(0,self.vel_y)


       
        


    def updateLocation(self, changeX, changeY):
        self.locationX += changeX
        self.locationY += changeY



    #def animate(self, direction, is_moving):


    



        
        

