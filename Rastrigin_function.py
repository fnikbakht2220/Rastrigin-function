#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
# Fitness function. The code maximizes the value of the fitness function
def Rastrigin_func(x_local):
    D=x_local.size     # size of Numpy vector x_local
    Rastrigin_i=[0]
    for i,x_i in enumerate(x_local):
        Rastrigin_i += x_i**2-10*np.cos(2*np.pi*x_i)
    Rastrigin_i += 10*D
    return Rastrigin_i 

