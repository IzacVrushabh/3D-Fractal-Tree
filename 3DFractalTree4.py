# FRACTAL TREE 3D-alternative coloured branch

import pygame
import os
import math
import pygame.gfxdraw

# colours co-ordination...(rgb value)
black, red, blue = (0, 0, 0), (255, 26, 26), (21, 71, 200)

# centered window screen...
os.environ["SDL_VIDEO_CENTERED"] = '1'
pygame.init()
pygame.display.set_caption("Fractal Tree 3D")

#window size...
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


def fractalTree(position, angle, z_value, n_value, direction, color=black, depth=0):
    branch_ratio = 0.3
    branch = z_value * branch_ratio
    angle_x = branch * math.cos(direction)
    angle_y = branch * math.sin(direction)
    (x, y) = n_value
    next_position = (x + angle_x, y + angle_y)
    pygame.draw.line(screen, color, n_value, next_position)

    if position > 0:
        if depth % 2 == 1:
            color1 = red
        else:
            color1 = blue

        new = z_value * (1 - branch_ratio)
        #recursive call....
        fractalTree(position-1, angle, new, next_position, direction-angle, color1, depth+1)
        fractalTree(position-1, angle, new, next_position, direction+angle+20, color1, depth+1)


speed = 0.01

def main():
    #pygame.gfxdraw.line(screen, 10, 9, 29, 50, red)
    angle = 0
    while True:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();

        angle += speed
        screen.fill(black)
        fractalTree(10, angle, height * 0.9, (width//2, width-50), -math.pi/2)
        #fractalTree(10, angle+1, height * 0.9, (width//2, width-50), -math.pi/2)
        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.QUIT
