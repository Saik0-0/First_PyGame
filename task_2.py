import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            coord = pygame.mouse.get_pos()

            if event.button == 1:
                pygame.draw.circle(screen, 'Blue', coord, 10)
                pygame.draw.rect(screen, 'Green', pygame.Rect(coord[0] - 5, coord[1] - 5, 10, 10))

            if event.button == 3:
                pygame.draw.circle(screen, 'Red', coord,10)

        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()