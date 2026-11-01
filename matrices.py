def path_length(path):

    if path is None:
        return 0

    return len(path)


def path_violation(path, grid):

    if path is None:
        return True

    for x, y in path:

        # Risk zone violation
        if grid[x][y] == 1:

            return True

    return False