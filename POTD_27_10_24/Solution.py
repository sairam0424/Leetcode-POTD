class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        m=len(matrix)

        n = len(matrix[0])

        ans = 0

        dp = [[0]*(n+1)for _ in range(m+1)]

        for i in range(1,m+1):

            for j in range(1,n+1):

                if matrix[i-1][j-1] == 1:

                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1

                    ans +=dp[i][j]

        return ans
        