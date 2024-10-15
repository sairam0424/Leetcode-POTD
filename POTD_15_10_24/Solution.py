class Solution:
    def minimumSteps(self, s: str) -> int:

        zero_pointer =  0 

        count = 0  

        for index , char in enumerate(s):

            if char == "0": 
                 
                count += index - zero_pointer

                zero_pointer+=1

        return count




        
        