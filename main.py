import pygame
from game_screen import game_screen

pygame.init()


# Initialize the game
screen_width = 1100
screen_height = 1000


run = True

# Main game loop
while run:
    game_screen(screen_width, screen_height)