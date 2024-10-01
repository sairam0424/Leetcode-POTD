class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        remainders = [element%k for element in arr]#get the remainders of the elements of the array

        remainders.sort()#sort them to use the two pointes approach for get the sum of remainders equal to k with any pair satisfy it

        left = 0

        n = len(arr)

        right  = n-1

        while left<n and remainders[left]==0:#move the starting or left pointres untill the non zero element is found

            left+=1

        if left%2==1:#special case if the left pointer is at the middle of the array where we can return False from here

            return False

        while left<right:#use the two pointer to get the sum of pairs with equal to the k remainders

            if remainders[left] +  remainders[right] !=k:#if the pair sum is not equal to k

                return False

            left+=1#else move both the pointers

            right-=1

        return True 