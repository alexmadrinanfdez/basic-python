def n_paths(grid: list[list[int]]) -> int:
    if not grid:
        return
    r = len(grid)
    c = len(grid[0])
    dp = [[0 for _ in range(c)] for _ in range(r)]
    # base cases
    dp[0][0] = 1 - grid[0][0] # initial square
    for i in range(1, r):
        # leftmost column
        dp[i][0] = dp[i-1][0] * (1 - grid[i][0])
    for j in range(1, c):
        # top row
        dp[0][j] = dp[0][j-1] * (1 - grid[0][j])
    # update the rest of the grid
    for i in range(1, r):
        for j in range(1, c):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) * (1 - grid[i][j])
    return dp[-1][-1]

if __name__ == "__main__":
    obstacle_grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert n_paths(obstacle_grid) == 2
    obstacle_grid = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]
    assert n_paths(obstacle_grid) == 0
    obstacle_grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert n_paths(obstacle_grid) == 6