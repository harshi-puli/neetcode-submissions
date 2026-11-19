class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        numIslands =  0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            visited.add((r,c))
            q = deque([(r, c)])

            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited:
                        if grid[nr][nc] == "1":
                            q.append((nr, nc))
                            visited.add((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    numIslands += 1

        return numIslands
        

