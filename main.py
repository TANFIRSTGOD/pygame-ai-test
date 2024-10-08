import pygame
import enemy

pygame.init()

BACKGROUND_COLOR = (0,0,0)
PRIMARY_COLOR = (255,255,255)
ENEMY_COLOR = (255,0,0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame ai test")

clock = pygame.time.Clock()
fps = 60

#player setup

playerx = 375
playery = 275
PLAYER_WIDTH = 25
PLAYER_HEIGHT = 25
player_rect = pygame.Rect(playerx, playery, PLAYER_WIDTH, PLAYER_HEIGHT)

#enemy setup

enemyx = 0
enemyy = 0
ENEMY_WIDTH = 18
ENEMY_HEIGHT = 18

enemySpeed = 1

enemy_rect = pygame.Rect(enemyx, enemyy, PLAYER_WIDTH, PLAYER_HEIGHT)

#enemy2 setup

enemyx2 = 800
enemyy2 = 0

enemy_rect2 = pygame.Rect(enemyx2, enemyy2, PLAYER_WIDTH, PLAYER_HEIGHT)

holdingA = False
holdingW = False
holdingD = False
holdingS = False

speed = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit
            elif event.key == pygame.K_a:
                holdingA = True
            elif event.key == pygame.K_w:
                holdingW = True
            elif event.key == pygame.K_d:
                holdingD = True
            elif event.key == pygame.K_s:
                holdingS = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                holdingA = False
            elif event.key == pygame.K_w:
                holdingW = False
            elif event.key == pygame.K_d:
                holdingD = False
            elif event.key == pygame.K_s:
                holdingS = False

    #Update player
    if holdingA:
        playerx -= speed
    if holdingW:
        playery -= speed
    if holdingD:
        playerx += speed
    if holdingS:
        playery += speed
        
    if holdingW and holdingD or holdingW and holdingA or holdingS and holdingD or holdingS and holdingA:
        speed = 1.25
    else:
        speed = 2
    
    #enemy update

    enemyx = enemy.trackTarget(enemyx, enemyy, enemySpeed, playerx, playery)[0]
    enemyy = enemy.trackTarget(enemyx, enemyy, enemySpeed, playerx, playery)[1]

    enemyx2 = enemy.trackTarget(enemyx2, enemyy2, enemySpeed, playerx, playery)[0]
    enemyy2 = enemy.trackTarget(enemyx2, enemyy2, enemySpeed, playerx, playery)[1]

    player_rect = pygame.Rect(playerx, playery, PLAYER_WIDTH, PLAYER_HEIGHT)
    enemy_rect = pygame.Rect(enemyx, enemyy, ENEMY_WIDTH, ENEMY_HEIGHT)
    enemy_rect2 = pygame.Rect(enemyx2, enemyy2, ENEMY_WIDTH, ENEMY_HEIGHT)

    #update collisions

    if player_rect.colliderect(enemy_rect) or player_rect.colliderect(enemy_rect2):
        PRIMARY_COLOR = (255,0,0)

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.rect(screen, PRIMARY_COLOR, player_rect)
    pygame.draw.rect(screen, ENEMY_COLOR, enemy_rect)
    pygame.draw.rect(screen, ENEMY_COLOR, enemy_rect2)

    pygame.display.flip()

    clock.tick(fps)

pygame.quit()