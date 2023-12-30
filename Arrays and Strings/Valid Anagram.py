#!/usr/bin/env python
# coding: utf-8

# In[3]:


def isAnagram(self, s: str, t: str) -> bool:
        '''
        In this function we have to check whether if two words are anagram of each other.

        Input s (str), t(str)
        o/p bool

        Example:-
        I/p : s = "anagram", t = "nagaram"
        o/p : True
        '''
        assert(type(s)==str)
        assert(type(t)==str)
        
        if len(s)!=len(t):
            return False

        s_pro = 1
        s_add = 0

        t_pro = 1
        t_add = 0
        count=0
        while count<len(s):

            s_pro *=ord(s[count])
            s_add +=ord(s[count])

            t_pro *=ord(t[count])
            t_add += ord(t[count])
            count+=1

        return True if s_pro == t_pro and s_add == t_add else False

