#!/usr/bin/env python
# coding: utf-8

# In[2]:


def uniquePaths(m: int, n: int) -> int:

    '''
    Given the two integers m and n, m and n are the dimensions of the grid, 
    return the number of possible unique paths that the we can take to reach the bottom-right corner 
    starting from the top left corner. Each step only allowing us to go right or to go downwards.
    
    I/p:- m (int), n (int) 
    
    o/p:- Matrix[0][0] (int)
    
    
    Example:- 
    Input: m = 3, n = 7
    Output: 28
    
    '''
    
    assert(type(m)==int and type(n)==int)
    Matrix = [[0 for i in range(n)] for i in range(m)]

    Matrix[-1][-1]=1

        
    for r in range(m-1,-1,-1):
        for c in range(n-1,-1,-1):
                
            if r == m-1 and c == n-1:
                continue

            if r == m-1:
                Matrix[r][c] = Matrix[r][c+1]
                continue
            if c == n-1:
                Matrix[r][c] = Matrix[r+1][c]
                continue

            Matrix[r][c] = Matrix[r+1][c]  + Matrix[r][c+1]



    return Matrix[0][0]


# In[4]:


uniquePaths(3, 7)


# In[ ]:




