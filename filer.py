import pygame, sys
pygame.init()

wid, hei = 1280, 900

x_player, y_player = wid/2, hei/2
speed_player_y = speed_player_x = 30

blocks = [
    (200, 200, 200, 150),
    (200, 550, 100, 250),
    (800, 200, 1, 350),
    (800, 550, 350, 1)
]

screen = pygame.display.set_mode((wid, hei), pygame.NOFRAME)
pygame.display.set_caption('TEST_ROOM')

def playerMove(player, blocks:list, speedX, speedY):
    playerX, playerY, playerWid, playerHei = player
    player_rect = pygame.Rect(playerX, playerY, playerWid, playerHei)
    left_move = right_move = up_move = down_move = True
    left_move1 = right_move1 = up_move1 = down_move1 = True

    for block in blocks:
        blockX, blockY, blockWid, blockHei = block

        block_right = pygame.Rect(blockX + blockWid, blockY, speedX, blockHei)
        block_left = pygame.Rect(blockX - speedX, blockY, speedX, blockHei)
        block_bottom = pygame.Rect(blockX, blockY + blockHei, blockWid, speedY)
        block_top = pygame.Rect(blockX, blockY - speedY, blockWid, speedY)

        block_right1 = pygame.Rect(blockX + blockWid, blockY, 1, blockHei)
        block_left1 = pygame.Rect(blockX - 1, blockY, 1, blockHei)
        block_bottom1 = pygame.Rect(blockX, blockY + blockHei, blockWid, 1)
        block_top1 = pygame.Rect(blockX, blockY - 1, blockWid, 1)

        left_move = left_move and not player_rect.colliderect(block_right)
        right_move = right_move and not player_rect.colliderect(block_left)
        up_move = up_move and not player_rect.colliderect(block_bottom)
        down_move = down_move and not player_rect.colliderect(block_top)

        left_move1 = left_move1 and not player_rect.colliderect(block_right1)
        right_move1 = right_move1 and not player_rect.colliderect(block_left1)
        up_move1 = up_move1 and not player_rect.colliderect(block_bottom1)
        down_move1 = down_move1 and not player_rect.colliderect(block_top1)
    if keys[pygame.K_LEFT]:
        if left_move:
            playerX -= speedX
        elif left_move1:
            playerX -= 1
    if keys[pygame.K_RIGHT]:
        if right_move:
            playerX += speedX
        elif right_move1:
            playerX += 1
    if keys[pygame.K_UP]:
        if up_move:
            playerY -= speedY
        elif up_move1:
            playerY -= 1
    if keys[pygame.K_DOWN]:
        if down_move:
            playerY += speedY
        elif down_move1:
            playerY += 1
    return playerX, playerY

run = True
while run:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    screen.fill((0,0,0))

    player_rect = pygame.Rect(x_player, y_player, 40, 70)
    pygame.draw.rect(screen, (255, 0, 0), player_rect)

    for block in blocks:
        x_rect, y_rect, wid_rect, hei_rect = block
        block_rect = pygame.Rect(x_rect, y_rect, wid_rect, hei_rect)
        pygame.draw.rect(screen, (0, 255, 255), block_rect)

    x_player, y_player = playerMove((x_player, y_player, 40, 70), blocks, speed_player_x, speed_player_y)

    pygame.time.Clock().tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()
