import pygame
import random
#test comment
#constants
sq_size = 32
screen_width = 640
screen_height = 512



def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((screen_width, screen_height))
        clock = pygame.time.Clock()
        running = True
        a = 2.5
        b = 2.5
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            for i in range(1, sq_size):
                pygame.draw.line(screen, (255, 0, 0), (i*sq_size, 0), (i*sq_size, 512))
                pygame.draw.line(screen, (255, 0, 0), (0, i * sq_size), (640, i * sq_size))
            screen.blit(mole_image, mole_image.get_rect(topleft=(a, b)))
            pygame.display.flip()
            clock.tick(60)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (x // 32 == a // 32) and (y // 32 == b // 32):
                    a = random.randrange(0, screen_width - sq_size, sq_size) + 2.5
                    b = random.randrange(0, screen_height - sq_size, sq_size) + 2.5


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
