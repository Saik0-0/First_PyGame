import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
# pygame.draw.circle(screen, 'Pink', (100, 200), 30)

x = 30
y = 30

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            coord = pygame.mouse.get_pos()
            print(coord)

        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()