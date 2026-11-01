def apply_risk_zone(grid, x, y, radius=2):

    for dx in range(-radius, radius + 1):
        for dy in range(-radius, radius + 1):

            nx = x + dx
            ny = y + dy

            # Check grid boundaries
            if (
                0 <= nx < grid.shape[0]
                and
                0 <= ny < grid.shape[1]
            ):

                # Mark danger zone
                grid[nx][ny] = 1

    return grid