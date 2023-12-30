#!/usr/bin/env python
# coding: utf-8

# In[1]:


def combinationSum(candidates, target):
    
    '''
    Given an array of distinct integers "candidates" and a target integer, this function
    returns a list of all unique combinations of candidates where the chosen numbers sum to target.
    
    I/p : candidates (List[int]), target int
    o/p : res List[int]
    
    Example:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.  These are the only two combinations.
    '''
    
    assert(type(candiates)==int and type(target)==int)
    for i in nums:
        assert(type(i)==int)
    
    res = []
    def backtrack(curr,target,index):
            
        if target==0:
            res.append(curr.copy())
            return

        if index>=len(candidates) or target<0:
            return


        curr.append(candidates[index])
        backtrack(curr,target-candidates[index],index)
        curr.pop()
        backtrack(curr,target,index+1)
            


        

    backtrack([],target,0)
    return res


# In[ ]:




