
# coding: utf-8

# ### Assignment4
# Write a Python program to find the volume of a sphere with diameter 12 cm.

# In[1]:


import math


# In[4]:


diameter = 12
r = diameter/2


# In[7]:


sphere_volume = (4/3) * math.pi * (r**3)


# In[11]:


print("Sphere Volume {V} cm^3".format(V=sphere_volume))

