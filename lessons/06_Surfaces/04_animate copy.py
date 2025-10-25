#next class I need to take all the scattered code used to make the frog and put that into a frog class that I will make.
#I will do the same for the aligator thing and then "animate" them, whatever that means 

#i started on this but need to keep working next week 


import pygame
from jtlgames.spritesheet import SpriteSheet
from pathlib import Path

images = Path(__file__).parent / 'images'
filename = images / 'spritesheet.png'  # Replace with your actual file path
cellsize = (16, 16)  # Replace with the size of your sprites
spritesheet = SpriteSheet(filename, cellsize)

#Frog class here
class Frog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.frog_index = 0
        spritesheet = SpriteSheet(filename, cellsize)
        self.frog_sprites = scale_sprites(spritesheet.load_strip(0, 4, colorkey=-1) , 4)
        self.image = self.frog_sprites[0]
        self.rect = self.frog_sprites[0].get_rect(center=(100, 100))
        self.frames_per_image = 5
        self.frog_index = 0
        #slef.image
        #self.rect
    def update(self):
        if pygame.time.get_ticks() % self.frames_per_image == 0: 
            self.frog_index = (self.frog_index + 1) % len(self.frog_sprites)
            self.image = self.frog_sprites[self.frog_index]

#. work on this next class

class Alligator(pygame.sprite.Sprite):
    #I need to keep working on this next time, but i brouhgt everything in here already
    def __init__(self):
        super().__init__()
        self.allig_sprites = scale_sprites(spritesheet.load_strip( (0,4), 7, colorkey=-1), 4)
        self.allig_index = 0
        self.frame_count = 1
        self.frames_per_image = 100
        
        if self.frame_count % self.frames_per_image == 0: 
            self.allig_index = (self.allig_index + 1) % len(self.allig_sprites)
    def draw_alligator(self, alligator, index):

        """Creates a composed image of the alligator sprites.

        Args:
            alligator (list): List of alligator sprites.
            index (int): Index value to determine the right side sprite.
        Returns:
            pygame.Surface: Composed image of the alligator.
        """
        
        index = index % (len(alligator)-2)
        
        width = alligator[0].get_width()
        height = alligator[0].get_height()
        composed_image = pygame.Surface((width * 3, height), pygame.SRCALPHA)

        composed_image.blit(alligator[0], (0, 0))
        composed_image.blit(alligator[1], (width, 0))
        composed_image.blit(alligator[(index + 2) % len(alligator)], (width * 2, 0))

        return composed_image
    # to do: add all the aligator stuff to this class!!!

def scale_sprites(sprites, scale):
    """Scale a list of sprites by a given factor.

    Args:
        sprites (list): List of pygame.Surface objects.
        scale (int): Scale factor.

    Returns:
        list: List of scaled pygame.Surface objects.
    """
    return [pygame.transform.scale(sprite, (sprite.get_width() * scale, sprite.get_height() * scale)) for sprite in sprites]

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Sprite Animation Test")

    # Load the sprite sheet
    spritesheet = SpriteSheet(filename, cellsize)
    
    # Load a strip sprites

    # Compose an image
    log = spritesheet.compose_horiz([24, 25, 26], colorkey=-1)
    log = pygame.transform.scale(log, (log.get_width() * 4, log.get_height() * 4))

    # Variables for animation

    frames_per_image = 6
    frame_count = 0

    # Main game loop
    running = True
    
    
    sprite_rect = pygame.Rect((screen.get_width() // 2, screen.get_height() // 2), (1,1))
    frog = Frog()
    alligator = Alligator()
    frog_group = pygame.sprite.GroupSingle(frog)
    while running:
        screen.fill((0, 0, 139))  # Clear screen with deep blue

        # Update animation every few frames

        
        # Get the current sprite and display it in the middle of the screen

        frog.update()
        frog_group.draw(screen)

        composed_alligator = alligator.draw_alligator(alligator.allig_sprites, alligator.allig_index)
        screen.blit(composed_alligator,  sprite_rect.move(0, 100))

        screen.blit(log,  sprite_rect.move(0, -100))


        # Update the display
        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Cap the frame rate
        pygame.time.Clock().tick(60)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
