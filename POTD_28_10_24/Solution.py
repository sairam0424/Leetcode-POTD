class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        nums.sort(reverse = True)

        seen = {}

        for i,x in enumerate(nums):

            if x*x in seen:

                seen[x] = seen[x*x] + 1

            else:

                seen[x] = 1

        
        ans = max(seen.values())

        if ans>=2:

            return ans

        return -1
        
        