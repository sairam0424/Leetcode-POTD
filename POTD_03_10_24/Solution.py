# brute force solution - passed 133/135 testcase with an TLE
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        total_sum = sum(nums)

        if total_sum%p==0:

            return 0

        n=len(nums)

        min_len = n 

        for i in range(n):

            sub_sum = 0

            for j in range(i,n):

                sub_sum+=nums[j]

                remaining_sum = (total_sum - sub_sum)%p

                if remaining_sum%p==0:

                    min_len =  min(min_len,j-i+1)

        if min_len == n:

            return -1


        return min_len