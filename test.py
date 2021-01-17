import numpy as np
from scipy.integrate import odeint
import matplotlib.pylab as plt
def F(y,t):
    dy=np.zeros(1)
    dy[0]=t
    return dy


t=np.arange(0,100,0.1)
y0=0
result=odeint(F,y0,t)
fig=plt.figure()

plt.plot([1,0],[3,2],'-o')
plt.show()