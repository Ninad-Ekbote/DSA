#!/usr/bin/env python
# coding: utf-8

# In[2]:


def twoSum(nums, target):
    
    '''
    Given an array of integers nums and an integer target, this function
    returns the indices of the two numbers such that they add up to target.
    
    I/P :- nums (list(int)), target (int)
    o/p :- [i,HashMap[nums[i]]] list(int)
    
    Example:- 
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
    
    Time Complexity:- O(n)
    Space Complexity:- O(n)
    
    '''
        
    HashMap = {}

    for i in range(len(nums)):

        if nums[i] in HashMap:
            return [i,HashMap[nums[i]]]

        HashMap[target-nums[i]] = i

