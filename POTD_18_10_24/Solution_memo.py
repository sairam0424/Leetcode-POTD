class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:


        def count_subset(nums,index,cur_or,target_or):

            if index == len(nums):

                return 1 if cur_or==target_or else 0

            if(index,cur_or) in memo:

                return memo[(index,cur_or)]

            count_without_includes = count_subset(nums,index+1,cur_or,target_or)

            count_with_includes = count_subset(nums,index+1,cur_or | nums[index] , target_or)

            memo[(index,cur_or)] = count_without_includes + count_with_includes

            return memo[(index,cur_or)]


        max_or_value = 0

        for num in nums:

            max_or_value |= num

        memo={}
        
        return count_subset(nums,0,0,max_or_value)
        