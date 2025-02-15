class Solution:
    def punishmentNumber(self, n: int) -> int:


        def findPartition(startInd,curSum,stringNum,target):

            if startInd == len(stringNum):

                return curSum == target

            if curSum>target:

                return False

            # if(startInd,curSum) in memo:

            #     return memo[(startInd,curSum)]

            if memo[startInd][curSum]!=-1:

                return memo[startInd][curSum] == 1

            partitionFound = False


            for curInd in range(startInd,len(stringNum)):

                curString = stringNum[startInd:curInd+1]

                curNum = int(curString)

                partitionFound = partitionFound or findPartition(curInd+1,curSum+curNum,stringNum,target)

                if partitionFound == True:

                    # memo[(startInd,curSum)] = True

                    memo[startInd][curSum] = 1

                    return True

            # memo[(startInd,curSum)] = False

            memo[startInd][curSum] = 0

            return False

                



        punishmentNumber = 0

        test = []

        for num in range(1,n+1):

            squaredNum = num*num

            stringNum = str(squaredNum)

            # memo = {}

            memo = [[-1]*(num+1) for i in range(len(stringNum)+1)]

            if findPartition(0,0,stringNum,num):

                punishmentNumber += squaredNum

                test.append(punishmentNumber)


        print(test)

        return punishmentNumber



        