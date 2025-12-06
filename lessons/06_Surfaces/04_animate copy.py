
import pygame
from jtlgames.spritesheet import SpriteSheet
from pathlib import Path
import math

images = Path(__file__).parent / 'images'
filename = images / 'spritesheet.png'  # Replace with your actual file path
cellsize = (16, 16)  # Replace with the size of your sprites
spritesheet = SpriteSheet(filename, cellsize)

#Frog class here
class Frog(pygame.sprite.Sprite,):
    def __init__(self):
        super().__init__()
        self.frog_index = 0
        spritesheet = SpriteSheet(filename, cellsize)
        self.frog_sprites = scale_sprites(spritesheet.load_strip(0, 4, colorkey=-1) , 4)
        self.image = self.frog_sprites[0]
        self.rect = self.frog_sprites[0].get_rect(center=(100, 100))
        self.last_frame = 0
        self.direction_vector = pygame.math.Vector2(100, 0)  # Initial direction vector
        self.position = pygame.math.Vector2()
        self.jumped = False
        #slef.image
        #self.rect
    def update(self):
        if pygame.time.get_ticks() - self.last_frame > 200: 
            self.frog_index = (self.frog_index + 1) % len(self.frog_sprites)
            self.image = self.frog_sprites[self.frog_index]
            self.last_frame = pygame.time.get_ticks()

#. work on this next class

class Alligator(pygame.sprite.Sprite):
    #I need to keep working on this next time, but i brouhgt everything in here already
    def __init__(self):
        super().__init__()
        self.index = 0
        self.allig_sprites = scale_sprites(spritesheet.load_strip( (0,4), 7, colorkey=-1), 4)
        self.allig_index = 0
        self.frame_count = 1
        self.last_frame = 0
        self.draw_alligator(self.allig_sprites,self.allig_index)
        self.rect = self.allig_sprites[0].get_rect(center=(100, 100))
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
        
        self.index = self.index % (len(alligator)-2)
        
        width = alligator[0].get_width()
        height = alligator[0].get_height()
        composed_image = pygame.Surface((width * 3, height), pygame.SRCALPHA)

        composed_image.blit(alligator[0], (0, 0))
        composed_image.blit(alligator[1], (width, 0))
        composed_image.blit(alligator[(index + 2) % len(alligator)], (width * 2, 0))

        self.image = composed_image
    def update(self, frog):
        if pygame.time.get_ticks() - self.last_frame > 200: 
            self.allig_index = (self.allig_index + 1) % len(self.allig_sprites)
            self.draw_alligator(self.allig_sprites, self.allig_index)
        new_pos = pygame.Vector2(self.rect.y, self.rect.x).move_towards_ip(pygame.Vector2(frog.rect.y, frog.rect.x),1)


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
    alligator_group = pygame.sprite.GroupSingle(alligator)
    while running:
        screen.fill((0, 0, 139))  # Clear screen with deep blue

        # Update animation every few frames
        alligx = alligator.rect.x
        alligy = alligator.rect.y
        frogx = frog.rect.x
        frogy = alligator.rect.y

        if alligx < frogx:
            alligator.rect.x += 15
        elif alligx > frogx:
            alligator.rect.x -= 15
        if alligy < frogy:
            alligator.rect.y += 15
        elif alligy > frogy:
            alligator.rect.y -= 15
        # Get the current sprite and display it in the middle of the screen
        pygame.draw.line(screen, (0, 0, 120), frog.position, (100, 2))
        #it's complaining about the '100,' dunno how to fix
        frog.update()
        frog_group.draw(screen)
        alligator.update(frog)
        alligator_group.draw(screen)
        screen.blit(log,  sprite_rect.move(0, -100))
        pygame.draw.line(screen, (52, 137, 235), (frog.rect.x, frog.rect.y), (frog.rect.x + frog.direction_vector[0], frog.rect.y + frog.direction_vector[1]), 2)


        # Update the display
        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
 
            if event.type == pygame.QUIT:
                    running = False
        #arrow key movemnt to go here
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            frog.direction_vector = frog.direction_vector.rotate(-3)
        elif keys[pygame.K_RIGHT]:
            frog.direction_vector = frog.direction_vector.rotate(3)
        elif keys[pygame.K_DOWN]:
            frog.direction_vector.scale_to_length(frog.direction_vector.length()-1.0)
        elif keys[pygame.K_UP]:
            frog.direction_vector.scale_to_length(frog.direction_vector.length()+1.0)
        
        if keys[pygame.K_SPACE] and frog.jumped == False:
            frog.rect.x += frog.direction_vector[0]
            frog.rect.y += frog.direction_vector[1]
            frog.jumped = True
        elif not keys[pygame.K_SPACE]:
            frog.jumped = False
             

        # Cap the frame rate
        pygame.time.Clock().tick(60)

    # Quit Pygame
    pygame.quit()

### Might not work, might be in wrong place
    collider = pygame.sprite.spritecollide(Frog, Alligator, dokill=False)
    if collider:
        collider[0].explode()
        game_over = True
### Might be totally wrong

if __name__ == "__main__":
    main()
