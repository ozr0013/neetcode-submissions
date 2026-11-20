from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()

        def bfs(r, c):
            queue = deque([(r, c)])
            visit.add((r, c))
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols
                            and grid[nr][nc] == "1"
                            and (nr, nc) not in visit):
                        visit.add((nr, nc))
                        queue.append((nr, nc))

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    count += 1
                    bfs(r, c)
        return count