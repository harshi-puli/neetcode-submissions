class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # initialize the first row and first column as 1s
        paths = [[1] * n for _ in range(m)]

        print(paths)

        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

        return paths[m-1][n-1]
        