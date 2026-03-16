class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        res = 0
        visit = set()

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft() # change to q.pop to change to dfs instead of bfs
                dir = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in dir:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols)) and grid[r][c] == "1" and (r, c) not in visit:
                        q.append((r, c))
                        visit.add((r, c)) # add for set

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    res += 1
        return res