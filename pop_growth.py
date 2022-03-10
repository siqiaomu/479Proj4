#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
from scipy.integrate import solve_ivp
import pylab


# In[6]:


def pop_func(t, r, a_1 = 20, b_11 = 1, b_12 = 1, a_2 = 3, b_21 = 1, b_22 = 1):
    x, y = r
    fx = ( a_1 - b_11 * x - b_12 * y ) * x 
    fy = (-a_2 + b_21 * x - b_22 * y ) * y
    return np.array([fx, fy], float)

def pop_growth(t, dt, r0):
    t_eval = np.linspace(0, t, int(t/dt))
    sol = solve_ivp(pop_func, [0, t], r0, t_eval = np.linspace(0, t, int(t/dt)))
    return sol.y, t_eval


# In[ ]:




