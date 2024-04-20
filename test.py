import pygame
from pygame.locals import QUIT

import math
import pygame.draw

x = 0
y = 0

pygame.init()
screen = pygame.display.set_mode((600, 450))
pygame.display.set_caption('gaem')


def draw_rectangle(x, y, width, height, color, rotation=0):
    points = []

    # The distance from the center of the rectangle to
    # one of the corners is the same for each corner.
    radius = math.sqrt((height / 2)**2 + (width / 2)**2)

    # Get the angle to one of the corners with respect
    # to the x-axis.
    angle = math.atan2(height / 2, width / 2)

    # Transform that angle to reach each corner of the rectangle.
    angles = [angle, -angle + math.pi, angle + math.pi, -angle]

    # Convert rotation from degrees to radians.
    rot_radians = (math.pi / 180) * rotation

    # Calculate the coordinates of each point.
    for angle in angles:
        y_offset = -1 * radius * math.sin(angle + rot_radians)
        x_offset = radius * math.cos(angle + rot_radians)
        points.append((x + x_offset, y + y_offset))

    screen.fill((255, 255, 255))
    pygame.draw.polygon(screen, color, points)

angle=0

while True:
    angle -= 0.1
    x1, y1 = pygame.mouse.get_pos()
    x += (x1 - x) / 240
    y += (y1 - y) / 240
    draw_rectangle(x, y, 10, 10, '#216BFF', rotation=angle)
    print(x)
    print(y)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.display.flip()
    