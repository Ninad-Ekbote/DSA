#!/usr/bin/env python
# coding: utf-8

# In[2]:


def longestConsecutive(nums) -> int:
    '''
    Given an unsorted array of integers nums, this function returns 
    the length of the longest consecutive elements sequence.
    
    Args:-
    nums [List[nums]]
    
    Example:-
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
    
    Time Complexity :- O(n)
    Space Complexity :- O(n)
    
    '''
        
        curr_set = set(nums)

        
        longest = 0
        length = 0
        for i in nums:

            if i-1 not in curr_set:
                #print('t')
                length = 0

                while i+length in curr_set:
                    #print('i')
                    length+=1
                    

                longest = max(longest, length)


        return longest

