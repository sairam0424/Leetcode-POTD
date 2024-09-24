#3043 : Find the Length of Longest Common Prefix:   

import List  # type: ignore
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        #Longest common prefix :  given the two array of numuber and need to return the longest common prefix from the both arrays :

        #1 We start with the basic verison of the problem using the given string as the input which is called as the longest common prefix:

        #firstly comming to the longest common prefix we mainly deal this with the syings where we use the comparision of the both strings and we return longest common prefix we can found from the two strings given and for this we can use the lateral string comprassion and we use the time of the O(Max(string1 ,  string 2))

        #first follow up would be if given an arrays of the string as the input and need to return the longest common prefix between the two array of the string and we can use the similar approach to the first one where:

        #brute force approach would be using the each pair of the string and generating the lCP from the two string and storing it into an array ds and return the longest of the lcf we have found so far:

        #an slight optimizing would be using the min max of the stiring we can take the minimum length string form one array and check the lcf from the other array and return the maximum we can found os far this will slightly optimize the approache in the place of the time and space we are using in the  bruter force approach:

        #Other follow up would be dealing with the number and when they are given as the number and need to return the longest common prefix  we have found from the two arrays a:

        #in this approach we choose one array add all the prefix of the current number into an hashset or the hashmap to make the lookup very faster::

        #we use the hashset to make the look up of the prefix faster and make it smooth;

        #so first we add the prefix of the set called as the prefix set as form the longest to shorest and use the set to remove the duplicates :

        #then we loop over the another array number and their correspoinding prefix and generate them and then we kind of check if the prefix is seen in the hashset form the long to short to make it easy and store the len of it ussing the string conversion and store it in res:

        #return the maximum lpf we have found so far:

        #TC-> O(mlogM + nlogN)  m-> length of arr1 ,n -> length of the arr2 , M-> maximum value in arr1 and N->maxmimum value in arr2

        #SC->O(mlogM):

        #optimized approach(kindoff not well optimized in some cases) -> we can use the trie (prefix trees) which is use to store and lookup of the prefix of the string of number in an very fast approach : 


        prefix_set = set()#store the prefix of the num of first array

        for num in arr1:

            while num and num not in prefix_set:

                prefix_set.add(num)#prefix add 

                num//=10

        res = 0

        for num in arr2:#lcp using the hashset lookup

            while num and num not in prefix_set:

                num//=10

            if num in prefix_set:#get the maximum if the prefix is already in the queue

                res =  max(res,len(str(num)))

        return res
        