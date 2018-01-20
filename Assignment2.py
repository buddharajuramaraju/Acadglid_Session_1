
# coding: utf-8

# ### Session1
# Assignment-2
# Problem Statement
# 
# Write a program which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be
# printed in a comma-separated sequence on a single line.
# 

# In[7]:


result = []


# In[8]:


for one_number in range(2000,3201):
    if one_number % 7 == 0 and one_number % 5 !=0:
        result.append(one_number)


# In[10]:


print(",".join([str(x) for x in result]))

