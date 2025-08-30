"""
Example of loading a background image that is not as wide as the screen, and
tiling it to fill the screen.

"""
import pygame
import random
# Initialize Pygame
pygame.init()

from pathlib import Path
assets = Path(__file__).parent / 'images'

# Set up display
screen_width = 600
screen_height = 600
BLACK = 0,0,0
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tiled Background')

#heigt 600, width 100
#draw colored rectangles

def make_tiled_bg(screen, bg_file):
    # Scale background to match the screen height
    
    bg_tile = pygame.image.load(bg_file).convert()
    
    background_height = screen.get_height()
    bg_tile = pygame.transform.scale(bg_tile, (bg_tile.get_width(), screen.get_height()))

    # Get the dimensions of the background after scaling
    background_width = bg_tile.get_width()

    # Make an image the is the same size as the screen
    image = pygame.Surface((screen.get_width(), screen.get_height()))

    # Tile the background image in the x-direction
    for x in range(0, screen.get_width(), background_width):
        image.blit(bg_tile, (x, 0))
        
    return image

def make_color_tiles(screen):
    
    background_height = screen.get_height()

    # Get the dimensions of the background after scaling
    background_width = 87

    # Make an image the is the same size as the screen
    image = pygame.Surface((screen.get_width() * 2, screen.get_height()))

    # Tile the background image in the x-direction
    for x in range(0, screen.get_width(), background_width):
        pygame.draw.rect(image, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (x, 0, background_width, background_height))
        pygame.draw.rect(image, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (x + screen.get_width(), 0, background_width, background_height))
        
    return image  

        



background = make_tiled_bg(screen, assets/'background_tile.gif')
background = make_color_tiles(screen)
# Main loop
running = True
x=0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(x,0))

    x -= 1
        
    if x <= -screen_width:
        x = 0
    #pygame.draw.rect(screen, BLACK, color_tile)
    #Update the display
    pygame.display.flip()
    print(".")

# Quit Pygame
pygame.quit()
