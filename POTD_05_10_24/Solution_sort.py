#approach 1: gen all per  (TLE):

#aAppraoch 2: using sorting the substring and compare it with the s1 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1 = "".join(sorted(list(s1)))

        k = len(s1)

        for i in range(len(s2)):

            sub = s2[i:i+k]

            sort_sub = "".join(sorted(list(sub)))

            if sort_sub == s1:

                return True

        return False