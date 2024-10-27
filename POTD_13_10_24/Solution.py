import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        k = len(nums)

        left = right = nums[0][0]

        min_heap = []

        for i in range(k):

            list_ = nums[i]

            left = min(left,list_[0])

            right = max(right,list_[0])

            heapq.heappush(min_heap , (list_[0] , i ,0)) #min of list , index of min , element place in list

        res = [left,right]

        while True : 

            element , ind , inside_ind = heapq.heappop(min_heap)

            inside_ind+=1

            if inside_ind == len(nums[ind]):

                return res

            next_val = nums[ind][inside_ind]

            heapq.heappush(min_heap , ( next_val , ind , inside_ind))

            right = max(right , next_val)

            left  = min_heap[0][0]

            if right-left < res[1] - res[0]:

                res = [left,right]


        return res
