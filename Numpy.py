#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# numpy creating array

# In[36]:


a=np.array([1,2,3,4,5])
a=np.arange(1,10)
a=np.arange(1,10,2)
a=np.linspace(1,20,10,retstep=True)
a=np.zeros(5)
a=np.zeros((5,5))
a=np.ones((5,5))
a=np.identity(5)
print(a)


# Random Function

# In[48]:


a=np.random.random(size=10)
a=np.random.randint(1,10,5)
a=np.random.randint(1,17,size=(4,4))
print(a)


# Array index and slicing

# In[63]:


a[0]
a[0][1]
a[0:2][0]#it will select 0-1 row and 0 col
a[0:3][2]#it will select 0-2 row and 2 col
a[:,1]# selct all rows 1 column
a[:,1:3]#all rows and 1-2 column
a[0:2,3]#0-1 rows and 3 column
a[0:3,::2]#0-2 rows and all column but alternate elements


# Shape and reshape function

# In[74]:


a.shape
a=np.arange(1,11)
a=np.reshape(a,-1)
print(a[0])


# In[65]:


a.reshape(3,3)


# Some usefull function in numpy

# In[82]:


a.flatten()
np.sort(a)
np.mean(a)
np.median(a)
np.argmax(a)
np.argmin(a)


# Plot a graph with matplotlib.pyplot

# In[92]:


x=np.arange(1,20)
y=x**2
print(x,y)
#plt.scatter(x,y)
plt.figure(figsize=(10,8),dpi=60)
plt.bar(x,y,color='blue',align="center")
plt.show()


# In[ ]:




