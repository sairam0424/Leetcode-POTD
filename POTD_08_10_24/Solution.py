class Solution:
    def minSwaps(self, s: str) -> int:

        stack = []

        unbalanced = 0

        for char in s:

            if char == "[":

                stack.append("[")

            else:

                if len(stack)!=0 and stack[-1]=="[":

                    stack.pop()

                else:

                    unbalanced+=1
                    
        print(unbalanced)

        print(stack)

        return (unbalanced+1)//2


        