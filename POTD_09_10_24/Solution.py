class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []

        unbalanced = 0

        for char in s:

            if char == "(":

                stack.append("(")


            else:

                if stack:

                    stack.pop()

                else:

                    unbalanced+=1

        return unbalanced + len(stack)