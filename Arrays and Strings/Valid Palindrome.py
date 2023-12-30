#!/usr/bin/env python
# coding: utf-8

# In[3]:


def isPalindrome(self, s: str) -> bool:
    
    '''
    This function checks whether a string is a Palindrome or not.
    
    Input:- s (str)
    output:- bool
    
    Example:- 
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
    
    '''
    assert(type(s)==str)

    start = 0
    end = len(s)-1

        #check =True

    while(start<end):
           
        while start<end and not self.alphanum(s[start]):
            start+=1

        while start<end and not self.alphanum(s[end]):
            end-=1
        

        if(s[start].lower()!=s[end].lower()):
                
            return False

            start+=1
            end-=1


        return True


    def alphanum(self, c:str)->bool:

        
        return (ord('A')<=ord(c)<=ord('Z') or 
                ord('a')<=ord(c)<=ord('z') or 
                ord('0')<=ord(c)<=ord('9'))


# In[ ]:




