class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:

        def dfs(robo_ind,fact_ind,robot,fact_pos):

            if robo_ind == len(robot):

                return 0

            if fact_ind == len(fact_pos):

                return float('inf')

            take = abs(robot[robo_ind]-fact_pos[fact_ind])+dfs(robo_ind+1,fact_ind+1,robot,fact_pos)

            not_take = dfs(robo_ind,fact_ind+1,robot,fact_pos)

            return min(take,not_take)


        robot.sort()

        factory.sort()

        pos = [] 

        for fact in factory:

            for i in range(fact[1]):

                pos.append(fact[0])

        return dfs(0,0,robot,pos)


