class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        need_sum = sum(nums)%p

        map = {0:-1}

        cur_sum = 0

        res = n = len(nums)

        for i,j in enumerate(nums):

            cur_sum = (cur_sum+j) % p

            map[cur_sum] = i

            if (cur_sum-need_sum)%p in map:

                res = min(res, i-map[(cur_sum-need_sum)%p])

        if res == n:

            return -1

        return res