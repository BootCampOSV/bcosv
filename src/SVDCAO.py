
# coding: utf-8


import numpy as np 
from numpy.linalg import svd
import matplotlib.pyplot as plt
import pylayers.util.geomutil as geu
from mpl_toolkits.mplot3d import Axes3D



N = 200 
np.random.seed(1)
t = np.linspace(0,2*np.pi,N)
x = 10*np.cos(t)[None,:]
y = 20*np.sin(t)[None,:]
z = 30*(1-t/np.pi)[None,:]
pts1 = np.vstack((x,y,z)).T
print pts1.shape
ptm=np.mean(pts1,axis=0)
pts1 = pts1 - ptm
M = geu.MEulerAngle(0,2.4,.24)
pts2 = np.dot(pts1,M.T)



U1,S1,V1=svd(pts1)
U2,S2,V2=svd(pts2)


# In[4]:

x1_r= S1[0]*U1[:,0]
y1_r= S1[1]*U1[:,1]
z1_r= S1[2]*U1[:,2]
pts1_r= np.vstack((x1_r,y1_r,z1_r)).T
x2_r= S2[0]*U2[:,0]
y2_r= S2[1]*U2[:,1]
z2_r= S2[2]*U2[:,2]
pts2_r= np.vstack((x2_r,y2_r,z2_r)).T


# In[5]:

np.dot(M,M.T)


# In[6]:

S1


# In[7]:

S2


# In[8]:

fig1 = plt.figure()
ax1 = fig1.add_subplot(111,projection='3d')
ax1.scatter(pts1[:,0],pts1[:,1],pts1[:,2],s=20,color='g')
ax1.scatter(pts2[:,0],pts2[:,1],pts2[:,2],s=20,color='b')
ax1.scatter(pts1_r[:,0],pts1_r[:,1],pts1_r[:,2],s=20,color='r')
ax1.scatter(pts2_r[:,0],pts2_r[:,1],pts2_r[:,2],s=20,color='r')


# In[9]:

U1


# In[10]:

U2


# In[11]:

np.linalg.det(V2)


# On est bon à une symmétrie près

# In[ ]:



