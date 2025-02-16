from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        arr = [0] * (2 * n - 1)

        i = 0

        vis = [False] * (n + 1)  # to check if we have used the current number

        def dfs(arr, i, vis):

            if i >= 2 * n - 1:  # array filled

                return True

            for num in range(n, 0, -1):  # loop and try the num from n to 1
                # two cases:
                # num > 1, we check two places. Mind index out of bound here.
                # num = 1, we only check one place
                # arr[i] == 0 means index i is not occupied
                if (
                    num > 1
                    and (
                        arr[i] != 0
                        or i + num >= 2 * n - 1
                        or arr[i + num] != 0
                        or vis[num]
                    )
                    or (num == 1 and (arr[i] != 0 or vis[num]))
                ):

                    continue

                # if num can be taken into action then place into the res arr

                if num > 1:  # if num>1 we can place it at two cases

                    arr[i] = num

                    arr[i + num] = num

                else:

                    arr[i] = num

                vis[num] = True  # make the num visited

                nexti = i + 1  # find the next available plce

                while nexti < 2 * n - 1 and arr[nexti]:

                    nexti += 1

                if dfs(arr, nexti, vis):  # use the dfs rec to place the next num

                    return True

                if (
                    num > 1
                ):  # backtracking -- if not valid restore the previous state by replace the placed element into zero and making them un visited

                    arr[i] = 0

                    arr[i + num] = 0

                else:

                    arr[i] = 0

                vis[num] = False

            return False

        dfs(arr, i, vis)

        return arr
