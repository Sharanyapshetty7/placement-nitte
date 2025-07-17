grid = [[" " for i in range(10)] for i in range(10)]
for i in range(10):
    for j in range(10):
        if j == 0 or j == 9 or (i == j and i < 5) or (i + j == 8 and i < 5):
            grid[i][j] = "*"
for row in grid:
    print(" ".join(row))
