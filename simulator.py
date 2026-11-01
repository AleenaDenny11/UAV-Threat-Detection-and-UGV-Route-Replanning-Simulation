import pygame
import numpy as np
import time

from detector import generate_threats
from messaging import (
    send_detection,
    receive_detection
)

from risk import apply_risk_zone
from planner import astar

from matrices import (
    path_length,
    path_violation
)
# =========================
# GRID SETTINGS
# =========================

GRID_SIZE = 20
CELL_SIZE = 35

WINDOW_SIZE = GRID_SIZE * CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
GRAY = (200, 200, 200)
# =========================
# PYGAME SETUP
# =========================

pygame.init()

screen = pygame.display.set_mode(
    (WINDOW_SIZE, WINDOW_SIZE)
)

pygame.display.set_caption(
    "TACTI-SENSE Live Demo"
)

clock = pygame.time.Clock()
# =========================
# CREATE GRID
# =========================

grid = np.zeros((GRID_SIZE, GRID_SIZE))

start = (0, 0)
goal = (19, 19)

grid[start] = 2
grid[goal] = 3
# =========================
# GENERATE THREATS
# =========================

threats = generate_threats(5)

received_threats = []

print("\n=== UAV DETECTIONS ===\n")

for t in threats:

    message = send_detection(t)

    decoded = receive_detection(message)

    received_threats.append(decoded)

    print(decoded)
# =========================
# APPLY RISK ZONES
# =========================

for t in received_threats:

    x, y = t["location"]

    apply_risk_zone(
        grid,
        x,
        y,
        radius=2
    )

# Draw threats again
for t in received_threats:

    x, y = t["location"]

    grid[x][y] = 4

# Restore start/goal
grid[start] = 2
grid[goal] = 3
# =========================
# A* PLANNING
# =========================

path = astar(
    grid,
    start,
    goal
)

if path is None:

    print("No safe path found.")

    pygame.quit()
    exit()

# Draw path
for x, y in path:

    if grid[x][y] == 0:

        grid[x][y] = 5
# =========================
# METRICS
# =========================

print("\n=== METRICS ===\n")

print(
    "Path Length:",
    path_length(path)
)

print(
    "Risk Zone Violation:",
    path_violation(path, grid)
)
# =========================
# DRAW FUNCTION
# =========================

def draw_grid(robot_position=None):

    screen.fill(WHITE)

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):

            value = grid[x][y]

            color = WHITE

            # Safe
            if value == 0:
                color = WHITE
            # Risk zone
            elif value == 1:
                color = ORANGE

            # Start
            elif value == 2:
                color = GREEN

            # Goal
            elif value == 3:
                color = BLUE

            # Threat
            elif value == 4:
                color = RED
            # Planned path
            elif value == 5:
                color = YELLOW

            rect = pygame.Rect(
                y * CELL_SIZE,
                x * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            pygame.draw.rect(
                screen,
                color,
                rect
            )
            pygame.draw.rect(
                screen,
                BLACK,
                rect,
                1
            )

    # Draw robot
    if robot_position:

        rx, ry = robot_position

        robot_rect = pygame.Rect(
            ry * CELL_SIZE,
            rx * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )
        pygame.draw.rect(
            screen,
            PURPLE,
            robot_rect
        )

    pygame.display.update()
    # =========================
# LIVE ROBOT MOVEMENT
# =========================

running = True

step = 0

while running:

    clock.tick(5)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    # Animate robot
    if step < len(path):

        robot_position = path[step]
        draw_grid(robot_position)

        step += 1

    else:

        draw_grid(path[-1])

    pygame.display.flip()

pygame.quit()