class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        a = sorted(set(arr))

        d = {}

        for i,j in enumerate(a):

            d[j] = (i+1)

        res = [d[i] for i in arr]

        return res