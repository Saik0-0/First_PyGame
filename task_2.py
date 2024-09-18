import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

done = False

flag_blue = 0
flag_red = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                coord_left = pygame.mouse.get_pos()

                if flag_blue == 1:
                    screen.fill((0, 0, 0))
                    pygame.draw.circle(screen, 'Blue', coord_left, 10)
                    pygame.draw.rect(screen, 'Green', pygame.Rect(coord_left[0] - 5, coord_left[1] - 5, 10, 10))
                    # pygame.draw.circle(screen, 'Red', coord_right, 10)
                else:
                    flag_blue = 1

                pygame.draw.circle(screen, 'Blue', coord_left, 10)
                pygame.draw.rect(screen, 'Green', pygame.Rect(coord_left[0] - 5, coord_left[1] - 5, 10, 10))

            if event.button == 3:
                coord_right = pygame.mouse.get_pos()

                if flag_blue == 1:
                    screen.fill((0, 0, 0))
                    # pygame.draw.circle(screen, 'Blue', coord_left, 10)
                    # pygame.draw.rect(screen, 'Green', pygame.Rect(coord_left[0] - 5, coord_left[1] - 5, 10, 10))
                    pygame.draw.circle(screen, 'Red', coord_right, 10)
                else:
                    flag_blue = 1

                pygame.draw.circle(screen, 'Red', coord_right, 10)

        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()