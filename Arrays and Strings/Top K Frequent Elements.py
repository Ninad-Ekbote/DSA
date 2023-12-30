#!/usr/bin/env python
# coding: utf-8

# In[6]:


def topKFrequent(nums, k):
    
    '''
    Given an integer array nums and an integer k, return the k most frequent elements.
    
    I/P:- nums List[int], k int
    O/P:- res List[int]
    
    Example:-
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
    
    Time complexity:-
    O(n)
    Space complexity:-
    O(n)
    '''

    HashMap = {}
       
    for i in nums:

        HashMap[i] = HashMap.get(i,0)+1
    freq = [[] for i in range(len(nums)+1)]

    for keys,value in HashMap.items():
        freq[value].append(keys)

    res = []
    for i in freq[::-1]:
        res = res + i
    return res[:k]


# In[ ]:




