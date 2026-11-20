class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return None

        ROWS, COLS = len(board), len(board[0])
        visited = set()
        directions = [(-1, 0),(1, 0),(0,-1),(0,1)]

        safe = {
            (r, c)
            for r in range(ROWS)
            for c in range(COLS)
            if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1
        }

        def bfs(r, c):
            region = [(r,c)]
            q = deque([(r,c)])
            visited.add((r, c))

            while q:
                cr, cc = q.popleft()

                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visited:
                        if board[nr][nc] == "O":
                            region.append((nr, nc))
                            q.append((nr,nc))
                            visited.add((nr,nc))
                            
                
            if not any(spot in safe for spot in region):
                for rr, rc in region:
                    board[rr][rc] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in visited:
                    bfs(r, c)
                