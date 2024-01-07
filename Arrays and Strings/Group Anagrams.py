#!/usr/bin/env python
# coding: utf-8

# In[2]:


def groupAnagrams(strs):
    
    '''
    Given an array of strings strings, this function groups the anagrams together. 
    
    Input:- strs (Lists[str])
    output:- res List[Lists[str]]
    
    Example:- 
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    
    Time Complexity:- O(n.m) where n is the number of strings and m is the maximum number of letters in a string
    Space Complexity:- O(n)
    
    '''

    HashMap = {}

    for word in strs:
        product = 1
        summation = 0
        for l in word:
            product *= ord(l)

            summation+=ord(l)

        if (product,summation) in HashMap:

            HashMap[(product,summation)].append(word)

        else:
            HashMap[(product,summation)] = [word]

    res = []
    for k,v in HashMap.items():

        res.append(v)

    return res

