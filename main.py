import pygame
from game_screen import GameScreen

pygame.init()

# Initialize the game
screen_width = 1100
screen_height = 1000

def main():
    game = GameScreen(screen_width, screen_height)
    if game.home_screen():
        game.run_game()

if __name__ == "__main__":
    main()
