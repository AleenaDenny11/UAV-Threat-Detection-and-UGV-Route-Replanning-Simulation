import sys
import os

sys.path.append(
    os.path.abspath("src")
)

import numpy as np

from planner import astar
from risk import apply_risk_zone


GRID_SIZE = 20


# Test 1
def test_no_threats():

    grid = np.zeros((GRID_SIZE, GRID_SIZE))

    start = (0, 0)
    goal = (19, 19)

    path = astar(grid, start, goal)

    assert path is not None


# Test 2
def test_single_threat():

    grid = np.zeros((GRID_SIZE, GRID_SIZE))

    apply_risk_zone(grid, 10, 10)

    start = (0, 0)
    goal = (19, 19)

    path = astar(grid, start, goal)

    assert path is not None


# Test 3
def test_multiple_threats():

    grid = np.zeros((GRID_SIZE, GRID_SIZE))

    apply_risk_zone(grid, 5, 5)
    apply_risk_zone(grid, 10, 10)
    apply_risk_zone(grid, 15, 15)

    start = (0, 0)
    goal = (19, 19)

    path = astar(grid, start, goal)

    assert path is not None


# Test 4
def test_blocked_path():

    grid = np.ones((GRID_SIZE, GRID_SIZE))

    start = (0, 0)
    goal = (19, 19)

    path = astar(grid, start, goal)

    assert path is None


# Test 5
def test_start_equals_goal():

    grid = np.zeros((GRID_SIZE, GRID_SIZE))

    start = (5, 5)
    goal = (5, 5)

    path = astar(grid, start, goal)

    assert path == [(5, 5)]


# Test 6
def test_edge_threat():

    grid = np.zeros((GRID_SIZE, GRID_SIZE))

    apply_risk_zone(
        grid,
        0,
        0,
        radius=1
    )

    start = (2, 2)
    goal = (19, 19)

    path = astar(grid, start, goal)

    assert path is not None


# Test 7
def test_large_number_of_threats():

    grid = np.zeros((GRID_SIZE, GRID_SIZE))

    for i in range(10):

        apply_risk_zone(grid, i, i)

    start = (0, 19)
    goal = (19, 0)

    path = astar(grid, start, goal)

    assert path is not None


# Test 8
def test_path_avoids_risk():

    grid = np.zeros((GRID_SIZE, GRID_SIZE))

    apply_risk_zone(grid, 10, 10)

    start = (0, 0)
    goal = (19, 19)

    path = astar(grid, start, goal)

    for x, y in path:

        assert grid[x][y] != 1