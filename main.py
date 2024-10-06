import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame ai test")

clock = pygame.time.Clock()
fps = 60

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit

    clock.tick(fps)

pygame.quit()