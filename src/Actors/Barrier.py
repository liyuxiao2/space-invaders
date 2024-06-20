import pygame
from .Objects import Objects
from .functions.collision import check_collision

class Barrier(Objects):
    def __init__(self, width, height, locationX, locationY, speed, images) -> None:
        super().__init__(width, height, locationX, locationY, speed, images[0])
        self.barrier_lives = 5
        self.images = images  # List of images for different states
        self.current_image_index = 0  # Start with the initial image

    def update_image(self):
        """Update the barrier's image based on remaining lives."""
        if self.barrier_lives > 0:
            self.current_image_index = 5 - self.barrier_lives
            self.image = self.images[self.current_image_index]

    def handle_collision(self, other_object):
        """Handle collision with another object."""
        if check_collision(self, other_object):
            self.barrier_lives -= 1
            if self.barrier_lives > 0:
                self.update_image()
            else:
                # Handle the barrier destruction or disappearance
                self.destroy()

    def destroy(self):
        """Handle the barrier's destruction."""
        # Code to remove the barrier from the game or mark it as destroyed
        pass

# Example usage
# Assuming `images` is a list of 5 pygame.Surface objects representing the barrier's different states.
# barrier = Barrier(width=100, height=20, locationX=50, locationY=50, speed=0, images=images)
