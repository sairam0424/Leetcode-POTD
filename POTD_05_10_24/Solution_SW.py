#approach 3 : using sliding window to get the substring and compare it with the s1 and make it more efficient using the two pointer variable sliding window 


from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        c1 = Counter(s1)

        left = 0

        k = len(s1)

        for right in range(len(s2)):

            c1[s2[right]]-=1

            while c1[s2[right]]<0:

                c1[s2[left]]+=1

                left+=1

            if right-left+1 == k:

                return True

        return False