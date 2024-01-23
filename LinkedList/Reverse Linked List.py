#!/usr/bin/env python
# coding: utf-8

# In[2]:


def reverseList(head):
    
    '''
    This function reverses a linked list
    
    Args:
        Input:- head (Optional[ListNode]) Linked list head
        
    Example:- 
    Input: head = [1,2]
    Output: [2,1]
    '''
    
    if head:
        if head.next:
            future = head.next
        else:
            return head
    else:

        return head

    prev = None

    start = head
    curr = head


    while future:

        curr.next = prev
        prev = curr
        curr = future
        future = future.next
    curr.next = prev
    return curr


# In[ ]:




