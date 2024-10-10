class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        n = len(nums)

        ind = [i for i in range(n)]

        ind.sort(key = lambda x : (nums[x],x))

        min_ind = n

        maxa = 0

        for i in ind:

            maxa = max(maxa , i-min_ind)

            min_ind = min(min_ind,i)        

        return maxa