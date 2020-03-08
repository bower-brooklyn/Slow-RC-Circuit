#!/usr/bin/env python
# coding: utf-8

# In[37]:


import numpy as np
import matplotlib.pyplot as plt


# In[38]:


V = np.array([0,3.58,5.98,7.57,8.70,9.40,9.77,9.99,10.11,10.18,10.24,10.31,10.37])
T = np.array([0,10,20,30,40,50,60,70,80,90,100,110,120])


# In[39]:


plt.plot(T,V, 'ro')
plt.ylabel("Volts")
plt.xlabel("time in seconds")
plt.title("Volts vs Time for a Charging Capacitor")
plt.show()


# In[40]:


v = np.array([12,8.21,5.59,3.89,2.71,1.86,1.31,.91,.65,.44,.31,.23,.16])
t = np.array([0,10,20,30,40,50,60,70,80,90,100,110,120])


# In[41]:


plt.plot(t,v, 'ro')
plt.ylabel("Volts")
plt.xlabel("time in seconds")
plt.title("Volts vs Time for a Discharging Capacitor")
plt.show()

