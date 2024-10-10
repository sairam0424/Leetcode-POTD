class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        stack = []

        n = len(nums)

        for ind,num in enumerate(nums):

            if not stack or nums[stack[-1]]>num:

                stack.append(ind)

        maxa = 0

        for i in range(n-1,-1,-1):

            while stack and nums[i]>=nums[stack[-1]]:

                maxa = max(maxa,i-stack.pop())

        return maxa

