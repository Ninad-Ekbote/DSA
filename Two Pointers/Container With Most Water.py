#!/usr/bin/env python
# coding: utf-8

# In[2]:


def maxArea(height):
    '''
    Given an integer array height of length n. 
    There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Any two vertical lines form a container.
    This function returns the maximum amount of water a container can store.
    
    Input: - height List[int]
    Ouput:- max_area int
    
    Example:- 
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    
    Time Complexity:- O(n)
    Space Complexity:- O(n) 
    '''
    
    l = 0
    r = len(height)-1

    max_area = 0

    while l<r:
            
        curr_height = (r-l)*min(height[l],height[r])

        max_area = max(max_area,curr_height)

        if height[l]<height[r]:
            l+=1
        else:
            r-=1

    return max_area

