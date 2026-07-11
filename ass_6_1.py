def print_groups(matrix):
    visited = set()

    def is_valid(i, j):
        return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])

    def dfs(i, j, group):
        if not is_valid(i, j) or (i, j) in visited or matrix[i][j] != group:
            return
        visited.add((i, j))
        print(f"({i},{j}) ", end="")
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(i + di, j + dj, group)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i, j) not in visited:
                print("Group:", end=" ")
                dfs(i, j, matrix[i][j])
                print()
matrix = [
    [1, 1, 2, 3],
    [1, 2, 2, 3],
    [4, 4, 4, 5],
    [6, 6, 6, 7]
]
print_groups(matrix)