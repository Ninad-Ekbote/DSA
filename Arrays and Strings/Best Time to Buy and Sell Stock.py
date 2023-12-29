#!/usr/bin/env python
# coding: utf-8

# In[3]:


def maxProfit(self, prices: List[int]) -> int:

        '''
        This function returns the maximum profit we can get from the given array.

        input:- prices (List[int])

        o/p:- max_profit (int)

        example:- 
        prices = [7,1,5,3,6,4]
        Output: 5
        '''

        if len(prices)==1:
            return 0

        l = 0
        r = 1
        max_profit = 0
        while r<len(prices):

            if prices[r]<prices[l]:
                l+=1

            if prices[l]<=prices[r]:
                max_profit = max(prices[r]-prices[l],max_profit)
                r+=1


        return max_profit

