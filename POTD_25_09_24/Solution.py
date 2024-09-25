from collections import defaultdict
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        res = []

        prefix_map = defaultdict(int)

        for word in words:

            for pointer in range(len(word)):

                curr_prefix  =  word[:pointer+1]

                prefix_map[curr_prefix]+=1

        for word in words:

            score = 0

            for pointer in range(len(word)):

                count = prefix_map[word[:pointer+1]]
                
                score+=count

            res.append(score)

        return res