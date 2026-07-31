class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        islands = []

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                spot = grid[r][c]

                if spot == 1:
                    top = grid[r-1][c]
                    bot = grid[r+1][c]
                    left = grid[r][c-1]
                    right = grid[r][c+1]

                    if not islands:
                        for i in range(len(islands)):
                            island = islands[i]

                            if bot in island or top in island or left in island or right in island:
                                island.append(spot)
                            else:
                                islands.append([spot])
                                count += 1
                                print(r)
                                print(c)
                    else:
                        islands.append([spot])
                        count += 1
                        print(r)
                        print(c)
        '''
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    
                    if (r in range(rows) and 
                        c in range(cols) and 
                        grid[r][c] == "1" and 
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands
                    




        return islands