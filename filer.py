import pygame, random, sys
pygame.init()
wid, hei = 1280, 900

x_player, y_player = wid/2, hei/2
speed_player_y = speed_player_x = 5
down_move = up_move = left_move = right_move = True

#короч, размер не меньше 5
x_rect1, y_rect1, wid_rect1, hei_rect1 = 200, 200, 200, 150
x_rect2, y_rect2, wid_rect2, hei_rect2 = 200, 550, 100, 250
x_rect3, y_rect3, wid_rect3, hei_rect3 = 800, 200, 5, 350
x_rect4, y_rect4, wid_rect4, hei_rect4 = 800, 550, 350, 5

def checkerMove(image, blocks):
    imageX, imageY, imageWid, imageHei = image
    image_rect = pygame.Rect(imageX, imageY, imageWid, imageHei)
    left_move = right_move = up_move = down_move = True
    for block in blocks:
        blockX, blockY, blockWid, blockHei = block

        block_right = pygame.Rect(blockX + blockWid, blockY, 1, blockHei)
        block_left = pygame.Rect(blockX - 1, blockY, 1, blockHei)
        block_bottom = pygame.Rect(blockX, blockY + blockHei, blockWid, 1)
        block_top = pygame.Rect(blockX, blockY - 1, blockWid, 1)

        left_move = left_move and not image_rect.colliderect(block_right)
        right_move = right_move and not image_rect.colliderect(block_left)
        up_move = up_move and not image_rect.colliderect(block_bottom)
        down_move = down_move and not image_rect.colliderect(block_top)

    return left_move, right_move, up_move, down_move

screen = pygame.display.set_mode((wid, hei))
pygame.display.set_caption("TEST_ROOM")

run = True

blocks = [
    (x_rect1, y_rect1, wid_rect1, hei_rect1),
    (x_rect2, y_rect2, wid_rect2, hei_rect2),
    (x_rect3, y_rect3, wid_rect3, hei_rect3),
    (x_rect4, y_rect4, wid_rect4, hei_rect4)
]

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

    left_move, right_move, up_move, down_move = checkerMove((x_player, y_player, 40, 70), blocks)

    if keys[pygame.K_LEFT] and left_move:
        x_player -= speed_player_x
    if keys[pygame.K_RIGHT] and right_move:
        x_player += speed_player_x
    if keys[pygame.K_UP] and up_move:
        y_player -= speed_player_y
    if keys[pygame.K_DOWN] and down_move:
        y_player += speed_player_y

    pygame.time.Clock().tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()
