#brute force aproach to checkt if substring is equal to the "AB" or "CD" and remove this form the string with all the instances 

#where for removal of the each instance we use the while loop untill the substring of  "AB" or "CD" is not found 
class Solution:
    def minLength(self, s: str) -> int:

        while "AB" in s or "CD" in s:

            if "AB" in s:

                s = s.replace("AB","")

            if "CD" in s:

                s = s.replace("CD","")

        return len(s)