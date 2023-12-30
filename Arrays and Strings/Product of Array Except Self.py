#!/usr/bin/env python
# coding: utf-8

# In[3]:


def productExceptSelf(self, nums: List[int]) -> List[int]:
    
    '''
    Given an integer array nums, this function returns an array answer such that answer[i] is equal to the product of all 
    the elements of nums except nums[i]
    
    I/p nums List[nums]
    o/p res List[nums]
    
    Example:-
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
    
    '''
        
        assert(type(nums)==list)
        assert(len(nums)>=2)
        
        for i in nums:
            assert(type(i)==int)
        
        if len(nums)==2:
            return nums[::-1]

        pre = [1 for i in nums]
        post = [1 for i in nums]


        for i in range(len(nums)):
            if i==0: 
                pre[i] = nums[i]
                continue

            pre[i] =  pre[i-1]*nums[i]

        


        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                post[i] = nums[i]
                continue

            post[i] =  post[i+1]*nums[i] 



        res = []

        for i in range(len(nums)):
            if i==len(nums)-1:
                res.append(pre[i-1])
                continue

            if i==0:
                res.append(post[i+1])
                continue

            
            res.append(pre[i-1]*post[i+1])

        return res


# In[ ]:




