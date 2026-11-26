class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1


        minutes = 0

        while q and fresh: 
            for _ in range(len(q)):
                cr, cc = q.popleft()
                
                for d in dirs:
                    if cr + d[0] in range(ROWS) and cc + d[1] in range(COLS): 
                        nr, nc = cr + d[0], cc + d[1]

                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
                            fresh -= 1
                            print((nr,nc))

            minutes += 1

        if fresh:
            return -1

        return minutes
        
