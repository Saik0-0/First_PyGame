import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
# pygame.draw.circle(screen, 'Pink', (100, 200), 30)

x = 30
y = 30

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((0, 0, 0))
            coord = pygame.mouse.get_pos()
            pygame.draw.circle(screen, 'Pink', (coord[0], 300), 8)
            for i in range(300 - coord[1]):
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, 'Pink', (coord[0], 300 - i), 8)
                pygame.display.flip()
                clock.tick(240)

            pygame.draw.circle(screen, 'Red', coord, 15)
            pygame.display.flip()
            pygame.time.delay(250)

            screen.fill((0, 0, 0))
            pygame.display.flip()

        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()