class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        count_a , count_b , count_c = 0 , 0 , 0

        res = []

        total_length = a+b+c 

        for i in range(total_length):

            max_count = max(a,b,c)

            if (a==max_count and count_a<2) or (count_b == 2 and a>=1) or (count_c == 2 and a>=1):

                res.append('a')

                a-=1

                count_a +=1

                count_b , count_c = 0,0

            elif (b==max_count and count_b<2) or (count_a == 2 and b>=1) or (count_c == 2 and b>=1):

                res.append('b')

                b-=1

                count_b+=1

                count_a , count_c = 0 ,0 

            elif (c == max_count and count_c<2) or (count_a==2 and c>=1) or (count_b == 2 and c>=1):

                res.append('c')

                c-=1

                count_c+=1

                count_a , count_b = 0,0
            
        return "".join(res)