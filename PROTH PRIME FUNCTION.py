#!/usr/bin/env python
# coding: utf-8

# ### Proth Numbers
# A **Proth number** is a number *N* of the form $N = k2^{n} + 1$ where *k* and *n* are positive integers, *k* is odd and $2^{n} > k$.
# 
# ### Proth Prime 
# A **Proth prime** is a proth number that is prime. 
# 
# Without the condition $2^{n} > k$, all odd numbers larger than 1 would be Proth numbers.
# 
# 

# To check if a number is a proth number, we first define a function to check if a number is a power of two.

# In[2]:


#function to check if the input is a power of two

def isPowerOfTwo(n):
    return (n and(not(n & (n-1))))


# In[3]:


isPowerOfTwo(4)


# In[4]:


isPowerOfTwo(6)


# The function below will check if the input is a  proth number or not

# In[5]:


def isProthNumber(n):
    k = 1
    while (k <(n//k)):
        
        #check if n is divisible by k
        if(n % k == 0):
            
            # checks if n/k is power of 2
            if(isPowerOfTwo(n//k)):
                return True
        
        # update k to the next odd number
        k = k + 2
        
    return False

# calling the function,
n = 9
if (isProthNumber(n-1)):
    print(f'{n} is a Proth number.')
else:
    print(f'{n} is not a Proth number.')


# In[6]:


# to return a list of proth numbers between two margins,
def print_Proth_Numbers(n_start, n_end):
    my_list = []
    for i in range(n_start, n_end):
        if (isProthNumber(i-1)) == True:
            my_list.append(i)
    print (my_list)


# In[7]:


my_list = print_Proth_Numbers(1, 20)


# In[29]:


# to check if a proth number is prime, I use a basic primality test since
# I haven't fully wrapped my head around the one posted on wikipedia.

def proth_prime(p):
    if (isProthNumber(p-1)):
        #trying to put primality test 
        if p <= 1:
            return False
        
        for factor in range(2, p):
            if p % factor == 0:
                return False
        return True
    else:
        print(f'{p} is not a proth number ')


# In[30]:


proth_prime(12)


# In[31]:


proth_prime(2)


# In[32]:


proth_prime(3)


# In[33]:


proth_prime(9)


# In[ ]:




