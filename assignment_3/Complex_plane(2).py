#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[4]:


def complex_plane(max_iter):
    x = np.linspace(-2, 2, 800)
    y = np.linspace(-2, 2, 800)
    X, Y = np.meshgrid(x, y)
    c = X + Y * 1j
    z = c.copy()
    divergent = np.full_like(c, False, dtype=bool)
    iterations = np.zeros_like(c, dtype=int)

    for i in range(max_iter):
        z[divergent] = 0
        z[~divergent] = z[~divergent] ** 2 + c[~divergent]
        divergent[np.logical_and(~divergent, np.abs(z) > 2)] = True
        iterations[np.logical_and(divergent, iterations == 0)] = i
    
    return divergent, iterations

