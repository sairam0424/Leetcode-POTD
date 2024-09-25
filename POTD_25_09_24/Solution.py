# The `Solution` class provides a method `sumPrefixScores` that calculates the sum of prefix scores
# for a list of words.
from collections import defaultdict
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:#this function returnt the list of the scores of the word of the words arr and get the score of all the prefix of the word of the array

        res = []

        prefix_map = defaultdict(int)#use the defaultdict as the map to store the count of the prefix as the key value pair of the prefix of the words of the strings

        for word in words:#get the score of the prefix of the word of the array

            for pointer in range(len(word)):#pointer method to get the prefix of the word 

                curr_prefix  =  word[:pointer+1]#calculate the correspoinding score with respect to the current prefix of the word arrayb 

                prefix_map[curr_prefix]+=1

        for word in words:#calcualte the score of each word of the array using of the prefix map which stores the count and the current prefix as the key value pair map: used the defaultdict to remove the key error:

            score = 0

            for pointer in range(len(word)):

                count = prefix_map[word[:pointer+1]]
                
                score+=count

            res.append(score)

        return res