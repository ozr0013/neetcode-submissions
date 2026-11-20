class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid) , len(grid[0])
        time, fresh = 0, 0
        q = collections.deque()
        neighbours = [[0,1], [0,-1], [1,0], [-1,0]]
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        while q and fresh > 0:
            for i in range((len(q))):
                r,c = q.popleft()
                for dr, dc in neighbours:
                    nr, nc = dr + r, dc + c
                    #make sure this is inbounds and its fresh
                    if nr in range(ROW) and nc in range(COL) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append([nr,nc])
                        fresh -= 1
            time += 1
        if fresh == 0:
            return time
        return -1