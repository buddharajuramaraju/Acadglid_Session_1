
# coding: utf-8

# ### Assignment3
# Write a Python program to accept the user's first and last name and then getting them
# printed in the the reverse order with a space between first name and last name.

# In[1]:


firstname = input ("First Name:")
lastname  = input ("Last Name:")


# In[3]:


print(firstname[::-1]+" "+lastname[::-1])

