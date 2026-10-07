class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0]) 
        maxArea = 0
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            area = 1

            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r in range(rows) and c in range(cols):
                        if grid[r][c] == 1 and (r,c) not in visited:
                            visited.add((r,c))
                            q.append((r,c))
                            area += 1

            return area
        
        for r in range(rows):
            for c in range(cols):
                if r in range(rows) and c in range(cols):
                    if grid[r][c] == 1 and (r,c) not in visited:
                        a = bfs(r,c)
                        if a > maxArea:
                            maxArea = a
        
        return maxArea
                    
                    

                    

