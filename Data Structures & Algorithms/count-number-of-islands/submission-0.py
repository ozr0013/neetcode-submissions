class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        ROWS, COLS = len(grid) , len(grid[0])
        visitSet = set()
        neighbors = [[1,0], [-1, 0], [0, -1], [0 , 1]]
        def bfs(r,c):
            q = collections.deque()
            visitSet.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for dr, dc in neighbors:
                    nr, nc = (row + dr), (col + dc)
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == "1" and (nr,nc) not in visitSet:
                        q.append((nr, nc))
                        visitSet.add((nr, nc))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visitSet:
                    bfs(r,c)
                    islands += 1
        return islands
 
        