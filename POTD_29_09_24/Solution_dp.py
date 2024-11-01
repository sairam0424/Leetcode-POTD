class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        dir = [-1,0,1]

       

        def dfs(grid,r,c):

            max_move = 0

            # if (r,c) in memo:

            #     return memo[(r,c)]

            if dp[r][c]!=-1:

                return -1

            for di in dir:

                nr,nc = r+dir[di] , c+1

                if 0<=nr<m and 0<=nc<n and grid[r][c]<grid[nr][nc]:

                    max_move= max(max_move,1+dfs(grid,nr,nc))

            # memo[(r,c)] = max_move

            dp[r][c] = max_move

            return max_move


        max_moves = 0

        n = len(grid[0])
        
        m = len(grid)

        memo = {}

        dp = [[-1]*(n+1) for i in range(m+1)]

        for i in range(m):

            cur_moves = dfs(grid,i,0)

            max_moves = max(max_moves,cur_moves)

        return max_moves


        