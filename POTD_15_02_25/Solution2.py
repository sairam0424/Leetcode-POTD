class Solution:
    def punishmentNumber(self, n: int) -> int:

        def dfs(stringNum,target):

            if not stringNum and target == 0:

                return True

            if target<0:

                return False

            partitionFound = False

            for ind in range(len(stringNum)):

                leftNum = stringNum[:ind+1]

                rightNum = stringNum[ind+1:]

                if dfs(rightNum,target-int(leftNum)):

                    return True


            return False

            


        punishmentNumber = 0

        for num in range(1,n+1):

            stringNum = str(num*num)

            if dfs(stringNum,num):

                punishmentNumber += int(stringNum)

        return punishmentNumber
        