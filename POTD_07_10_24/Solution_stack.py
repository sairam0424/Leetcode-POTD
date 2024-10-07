#an optimized approach is using the stack where we need to find the substrings "AB" and "CD" in the string s and remove all the instances of this substring and return the len of string s after this operations

#where we use the stack to store the single character and check for the conditions where if we find the cur char as the "B" or "D" and if we have the stack top as the "A" or "C" corresponding to the string with the substring they fore most

#corner case would be if not char in stack we just append of the char with any check condition :

# and at last we return the len of the stack as the length of the string

#TC -> O(N) , SC -> O(N)

class Solution:
    def minLength(self, s: str) -> int:

        stack = []

        for char in s:

            if not stack:

                stack.append(char)

            else:

                last = stack[-1]

                if last == "A" and char == "B":

                    stack.pop()

                elif last == "C" and char == "D":


                    stack.pop()

                else:

                    stack.append(char)


        return len(stack)
        