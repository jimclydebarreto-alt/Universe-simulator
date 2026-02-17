import pygame
import sys
from game import Game

def main():
    """Main entry point for the Universe Simulator game"""
    pygame.init()
    
    game = Game()
    game.run()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()