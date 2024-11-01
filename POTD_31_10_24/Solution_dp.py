class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:

        def dfs(robo_ind,fact_ind,robot,fact_pos):

            if robo_ind == len(robot):

                return 0

            if fact_ind == len(fact_pos):

                return float('inf')

            if(robo_ind,fact_ind) in memo:

                return memo[(robo_ind,fact_ind)]

            take = abs(robot[robo_ind]-fact_pos[fact_ind])+dfs(robo_ind+1,fact_ind+1,robot,fact_pos)

            not_take = dfs(robo_ind,fact_ind+1,robot,fact_pos)

            memo[(robo_ind,fact_ind)] = min(take,not_take)

            return memo[(robo_ind,fact_ind)]


        robot.sort()

        factory.sort()

        memo = {}

        pos = [] 

        for fact in factory:

            for i in range(fact[1]):

                pos.append(fact[0])

        return dfs(0,0,robot,pos)


