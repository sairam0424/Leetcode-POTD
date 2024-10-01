#this is solution for the problem which almost passes the 93/97 test cases

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        return sum(arr)%k==0