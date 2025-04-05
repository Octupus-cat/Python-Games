"""
Dino Jump

Use the arrow keys to move the blue square up and down to avoid the black
obstacles. The game should end when the player collides with an obstacle ...
but it does not. It's a work in progress, and you'll have to finish it. 

"""
import pygame
import random
from pathlib import Path

# Initialize Pygame
pygame.init()

images_dir = Path(__file__).parent / "images" if (Path(__file__).parent / "images").exists() else Path(__file__).parent / "assets"

# Screen dimensions
WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Jump")

# Colors
BLUE = (255, 255, 255)
BLACK = (0, 0, 50)
RED = (255, 0, 0)
WHITE = (0, 200, 250)

# FPS
FPS = 60

# Player attributes
PLAYER_SIZE = 10

player_speed = 5

# Obstacle attributes
OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 60
obstacle_speed = 5

# Font
font = pygame.font.SysFont(None, 36)


# Define an obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image = pygame.image.load(images_dir/"cactus_9.png")
        self.image = pygame.transform.scale(self.image,(OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = HEIGHT - OBSTACLE_HEIGHT

        self.explosion = pygame.image.load(images_dir / "explosion1.gif")

    def update(self):
        self.rect.x -= obstacle_speed
        # Remove the obstacle if it goes off screen
        if self.rect.right < 0:
            self.kill()

    def explode(self):
        """Replace the image with an explosition image."""
        
        # Load the explosion image
        self.image = self.explosion
        self.image = pygame.transform.scale(self.image, (OBSTACLE_WIDTH, OBSTACLE_WIDTH))
        self.rect = self.image.get_rect(center=self.rect.center)



# Define a player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(images_dir/"dino_0.png")
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = HEIGHT - PLAYER_SIZE - 10
        self.speed = player_speed
        self.jumping = False
    def update(self):
        keys = pygame.key.get_pressed()
        self.speed += 1
        self.rect.y += self.speed
        if keys[pygame.K_SPACE] and not self.jumping:
            self.speed = -15
            self.jumping = True


        # Keep the player on screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.jumping = False 

# Create a player object
player = Player()
player_group = pygame.sprite.GroupSingle(player)

# Add obstacles periodically
def add_obstacle(obstacles):
    # random.random() returns a random float between 0 and 1, so a value
    # of 0.25 means that there is a 25% chance of adding an obstacle. Since
    # add_obstacle() is called every 100ms, this means that on average, an
    # obstacle will be added every 400ms.
    # The combination of the randomness and the time allows for random
    # obstacles, but not too close together. 
    
    if random.random() < 0.5:
        obstacle = Obstacle()
        obstacles.add(obstacle)
        return 1
    return 0


# Main game loop
def game_loop():
    clock = pygame.time.Clock()
    game_over = False
    last_obstacle_time = pygame.time.get_ticks()

    # Group for obstacles
    obstacles = pygame.sprite.Group()

    #player_group = pygame.sprite.Group()

    obstacle_count = 0

    game = True
    while game:
        obstacles = pygame.sprite.Group()

    #player_group = pygame.sprite.Group()

        obstacle_count = 0

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Update player
            player.update()

            # Add obstacles and update
            if pygame.time.get_ticks() - last_obstacle_time > 500:
                last_obstacle_time = pygame.time.get_ticks()
                obstacle_count += add_obstacle(obstacles)
            
            obstacles.update()

            # Check for collisions
            collider = pygame.sprite.spritecollide(player, obstacles, dokill=False)
            if collider:
                collider[0].explode()
                game_over = True

        
            # Draw everything
            screen.fill(WHITE)
            player_group.draw(screen)
            obstacles.draw(screen)

            # Display obstacle count
            obstacle_text = font.render(f"Score: {obstacle_count}", True, BLACK)
            #game_over_text = font.render(f"GAME OVER", ,RED)
            screen.blit(obstacle_text, (10, 10))

            pygame.display.update()
            clock.tick(FPS)

    # Game over screen
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            screen.fill(BLUE)
            game_over_text = font.render(f"GAME OVER!", True, RED)
            screen.blit(game_over_text,(5,0))
            high_score_text = font.render(f"Final Score: {obstacle_count}", True, RED)
            screen.blit(high_score_text,(5,50))
            high_score_text = font.render(f"Click R to restart.", True, RED)
            screen.blit(high_score_text,(200,200)) 
            keys = pygame.key.get_pressed()
            print(keys)
            print(pygame.key.get_focused())
            if keys[pygame.K_r]:
                game = True
                game_over = False
                print("its doing the thing")
            clock.tick(FPS)
            pygame.display.update()
            
    

if __name__ == "__main__": 
    game_loop()
