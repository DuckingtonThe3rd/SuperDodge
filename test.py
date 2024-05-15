import pygame
from pygame.locals import QUIT

import math
import random
import pygame.draw

x = 0
y = 0

pygame.init()
screen = pygame.display.set_mode((600, 450))
pygame.display.set_caption('gaem')

def draw_rotated_rectangle(x, y, width, height, color, rotation=0):
    points = []

    # Hey rewamd i made some explanations for you
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

    pygame.draw.polygon(screen, color, points)

angle = 0

enemy_x = []
enemy_y = []

while True:
    screen.fill('#ababab')
    angle -= 2
    x1, y1 = pygame.mouse.get_pos()
    x += (x1 - x) / 50
    y += (y1 - y) / 50
    
    draw_rotated_rectangle(x, y, 10, 10, '#216BFF', rotation=angle)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    pygame.display.flip()
    
    for i in range(random.randint(0, 20)):
        enemy_x.append(random.randint(0, 600))

    if len(enemy_x) >= 0:
        for i in range(len(enemy_x)):
            enemy_x[i] += random.randint(-5, 5)
            enemy_y[i] += random.randint(0, 10)
            draw_rotated_rectangle(enemy_x[i], enemy_y[i], 10, 10, '#FF0000', rotation=angle)