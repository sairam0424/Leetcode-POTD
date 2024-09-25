#2416. Sum of Prefix Scores of Strings:

#given an array of the strings and need to find the corresponding score of the prefix of the string:

#1. Brute force approach :  in the bf approach we just loop over the entire word of the words array and store the prefix score of the word and store the count of visibility of the prefix in the map and at end loop over the relative words and calculate the score using the prefix_map and store the score of the correspoinding word:

#TC - > O(N*L*L) where the n->correspoinding to the no of words inside the array and l->length of the word of the array and this corresponds to the worst case time complexity using the hashmap to store the score of prefix:

#SC -> O(N)

#Optimized approach:we can cutoff the prefix score calculation of the words of the array : 

#so when any things come with the prefix and suffix of the string we can use the trie(prefix tree) which can perform better than the hashmap

#instead of using the hashmap we can use the trie(prefix tree) to store the corresponding score of the prefix of the word of the array: with the correspoinding score as the value and the prefix as the key in the trie:

#so we first construct the Trie class with the root as the prefix node and then we insert the word of the array into the trie and at the end we can calculate the score of the prefix of the word of the array using the trie:

#we just need to change the initilization of standard trie as the root children structure with the extra var to store of the count as the score of the prefix of the word of the array:

#we can fill the trie with the correspoinding word of the array and insert the prefix of the word of the array into the trie and also store the correspoinding score of the prefix in the trie:

#Trie Class will be structured as follows : 

#Intilization of the root - children map as 26(a-z) and the count as 0

#insert function will be used to insert the word of the array into the trie

#getscore function will be used to calculate the score of the prefix of the word of the array

#in the main fucntion we insert each prefix into the trie and get the correspoinding score of the prefix of the word of the array and add to the result array
 
class PrefixNode:#Prefix Node class to get the correspoinding of the Prefix tree

    def __init__(self):#This is the initilization of the Node class of the Prefix Node

        self.children = [None]*(26)#26(a-z) children of each node as the range fro a to z

        self.count = 0


class PrefixTree:#This is the PrefixTree class to get the tree class done:

    def __init__(self):#This is the initilization of the Prefix root of the Trie
        
        self.root = PrefixNode()

        

    def insert(self,word):#this is the insert function to insert the node into the trie structure:

        cur = self.root

        for character in word:

            index = ord(character) - ord('a')

            if not cur.children[index]:

                cur.children[index] = PrefixNode()

            cur = cur.children[index]

            cur.count +=1


    def getscore(self,word): #this is the getscore function to calcuate the score of the prefix of the word of the array

        cur = self.root

        score = 0

        for character in word:

            index = ord(character) - ord('a')

            cur = cur.children[index]

            score+=cur.count

        return score





class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:#sumprefixScore to calculate the score of the prefix of the word of the words array


        res = []

        prefix_tree = PrefixTree()#initilize the Prefix tree(Trie) Node 

        for word in words:#insert the word as into the correspoinding Prefix_tree(Trie)

            prefix_tree.insert(word)

        for word in words:#get the correspoinding score into the prefix_tree:

            res.append(prefix_tree.getscore(word))

        return res

        