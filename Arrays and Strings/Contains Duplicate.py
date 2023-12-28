#!/usr/bin/env python
# coding: utf-8

# In[3]:


def containsDuplicate(nums):
    
    '''
    This funtion checks if there are duplicates present in this array.
    
    Input nums: List[int]
    output True/False
    
    Example:- 
    Input nums = [1,2,3,1]
    Output True/False
    '''
    assert(type(nums)==list)
    for i in nums:
        assert(type(i)==int)
    
    hashset = set()
    for i in nums:

        if i not in hashset:
            hashset.add(i)
        else:
            return True

    return False

