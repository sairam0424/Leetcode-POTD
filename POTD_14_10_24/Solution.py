import heapq

from collections import deque

import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        

        max_heap = []

        for num in nums:

            heapq.heappush(max_heap , -num)

        ans = 0

        while k>0:

            max_element = -heapq.heappop(max_heap)

            ans += max_element

            heapq.heappush(max_heap,-math.ceil(max_element/3))

            k-=1

        return ans
        