import heapq


# Manhattan distance heuristic
def heuristic(a, b):

    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Get valid neighboring cells
def get_neighbors(node, grid):

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    neighbors = []

    for dx, dy in directions:

        nx = node[0] + dx
        ny = node[1] + dy

        # Stay inside grid
        if (
            0 <= nx < grid.shape[0]
            and
            0 <= ny < grid.shape[1]
        ):

            # Avoid risk zones
            if (
                grid[nx][ny] == 0
                or
                grid[nx][ny] == 3
            ):

                neighbors.append((nx, ny))

    return neighbors


# Reconstruct final path
def reconstruct_path(came_from, current):

    path = [current]

    while current in came_from:

        current = came_from[current]

        path.append(current)

    path.reverse()

    return path


# Main A* algorithm
def astar(grid, start, goal):

    open_set = []

    heapq.heappush(
        open_set,
        (0, start)
    )

    came_from = {}

    g_score = {
        start: 0
    }

    f_score = {
        start: heuristic(start, goal)
    }

    while open_set:

        current = heapq.heappop(open_set)[1]

        # Goal reached
        if current == goal:

            return reconstruct_path(
                came_from,
                current
            )

        for neighbor in get_neighbors(current, grid):

            tentative_g = g_score[current] + 1

            if (
                neighbor not in g_score
                or
                tentative_g < g_score[neighbor]
            ):

                came_from[neighbor] = current

                g_score[neighbor] = tentative_g

                f_score[neighbor] = (
                    tentative_g
                    +
                    heuristic(neighbor, goal)
                )

                heapq.heappush(
                    open_set,
                    (f_score[neighbor], neighbor)
                )

    # No valid path
    return None