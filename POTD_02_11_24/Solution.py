class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        arr = sentence.split()

        for i in range(1,len(arr)):

            first_char = arr[i][0]

            last_char = arr[i-1][-1]

            if first_char !=last_char:

                return False

        return arr[-1][-1] == arr[0][0]
