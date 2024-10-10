class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        maxa = 0

        n = len(nums)

        for i in range(n):

            for j in range(i+1,n):

                if nums[i]<=nums[j]:

                    maxa = max(maxa,j-i)

        return maxa