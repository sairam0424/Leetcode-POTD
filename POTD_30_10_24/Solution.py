class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:

        n=len(nums)

        if n<=3:

            return 0

        lis=[1]*(n)
        
        #lis=[0]*(n)

        for i in range(1,n):

            for j in range(i):

                if nums[i]>nums[j] and lis[j]+1>lis[i]:

                    lis[i]=1+lis[j]

        lds=[1]*(n)

        #lds=[0]*(n)

        for i in range(n-2,-1,-1):

            for j in range(n-1,i,-1):

                if nums[i]>nums[j] and lds[j]+1>lds[i]:

                    lds[i]=lds[j]+1

        maxa=0

        for i in range(n):

            #if lis[i]>0 and lds[i]>0:

            if lis[i]>1 and lds[i]>1:

                maxa=max(maxa,lis[i]+lds[i]-1)

        return n-maxa
        