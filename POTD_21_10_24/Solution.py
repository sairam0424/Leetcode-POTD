class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def dfs(s,start,seen):

            if start == len(s):

                return 0

            maxa = 0

            for end in range(start+1,len(s)+1):

                sub_string = s[start:end]

                if sub_string not in seen:

                    seen.add(sub_string)

                    maxa = max(maxa , 1+dfs(s,end,seen))

                    seen.remove(sub_string)


            return maxa

        seen = set()

        return dfs(s,0,seen)

        
        