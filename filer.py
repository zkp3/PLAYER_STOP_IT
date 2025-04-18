import pygame, sys
pygame.init()

wid, hei = 1280, 900

x_player, y_player = wid/2, hei/2
speed_player_y = speed_player_x = 50

blocks = [
    (200, 200, 200, 150),
    (200, 550, 100, 250),
    (800, 200, 1, 350),
    (800, 550, 350, 1)
]

screen = pygame.display.set_mode((wid, hei), pygame.NOFRAME)
pygame.display.set_caption('TEST_ROOM')

def playerMove(player, blocks, speedX, speedY):
    keys = pygame.key.get_pressed()
    playerX, playerY, playerWid, playerHei = player
    player_rect = pygame.Rect(playerX, playerY, playerWid, playerHei)

    def check_collision(blocks, player_rect, speedX, speedY):
        left_move = right_move = up_move = down_move = True
        for block in blocks:
            blockX, blockY, blockWid, blockHei = block

            left_move = left_move and not player_rect.colliderect(pygame.Rect(blockX + blockWid, blockY, speedX, blockHei))
            right_move = right_move and not player_rect.colliderect(pygame.Rect(blockX - speedX, blockY, speedX, blockHei))
            up_move = up_move and not player_rect.colliderect(pygame.Rect(blockX, blockY + blockHei, blockWid, speedY))
            down_move = down_move and not player_rect.colliderect(pygame.Rect(blockX, blockY - speedY, blockWid, speedY))

        return left_move, right_move, up_move, down_move

    if keys[pygame.K_LEFT]:
        orig_sdX = speedX
        while speedX > 0:
            left_move, _, _, _ = check_collision(blocks, player_rect, speedX, speedY)
            if left_move:
                playerX -= speedX
                break
            speedX -= 1
        speedX = orig_sdX

    elif keys[pygame.K_RIGHT]:
        orig_sdX = speedX
        while speedX > 0:
            _, right_move, _, _ = check_collision(blocks, player_rect, speedX, speedY)
            if right_move:
                playerX += speedX
                break
            speedX -= 1
        speedX = orig_sdX

    if keys[pygame.K_UP]:
        orig_sdY = speedY
        while speedY > 0:
            _, _, up_move, _ = check_collision(blocks, player_rect, speedX, speedY)
            if up_move:
                playerY -= speedY
                break
            speedY -= 1
        speedY = orig_sdY

    elif keys[pygame.K_DOWN]:
        orig_sdY = speedY
        while speedY > 0:
            _, _, _, down_move = check_collision(blocks, player_rect, speedX, speedY)
            if down_move:
                playerY += speedY
                break
            speedY -= 1
        speedY = orig_sdY

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

