#Approach 3 : Using Hashmap to count the freq of each char and compare it with the freq of the substring

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        c1 = Counter(s1)

        k = len(s1)

        for i in range(len(s2)):

            sub = s2[i:i+k]

            c2 = Counter(sub)

            if c1 == c2:

                return True

        return False



        