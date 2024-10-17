class Solution:
    def maximumSwap(self, num: int) -> int:

        maxa = num

        num_str = str(num)

        for i in range(len(num_str)):

            for j in range(i+1,len(num_str)):

                num_list = list(num_str)

                num_list[i] , num_list[j]  = num_list[j ] ,num_list[i]

                cur_num = int("".join(num_list))

                maxa = max(maxa,cur_num)

        return maxa