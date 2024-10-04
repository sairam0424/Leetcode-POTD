class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()#sort the skill array to pair the lowest with the highest skill using the two pointer kind off

        n = len(skill)

        total_chemistry = 0 #res

        target_team_skill = skill[-1] + skill[0] # default team skill which is the target we need to find 

        for i in range(n//2):#break the array into two half front and back of the array 

            if skill[i] + skill[-i-1] != target_team_skill: #check if the pair skill doesnt match with the target team skill then return -1 

                return -1

            total_chemistry+=(skill[i]*skill[-i-1]) #else calculate the total chemistry between the team(pair) players

        return total_chemistry#return the total_chemistry if the condition is satisfied



        