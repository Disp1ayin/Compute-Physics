from helm3d import  Helmholz
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pylab as plt


f=lambda x,y,z:x**2+y**2+z**2
g=lambda x,y,z:x**(1/2)
def bx0(y,z):
    return y**2+z**2

bxf=lambda y,z:16*np.cos(y)*np.cos(z)
by0=lambda x,z:x**2+z**2
byf=lambda x,z:16*np.cos(x)*np.cos(z)
bz0=lambda x,y:x**2+y**2
bzf=lambda x,y:16*np.cos(x)*np.cos(y)
x0=0
xf=4
y0=0
yf=4
z0=0
zf=4
Mx=100
My=100
Mz=100
D=[x0,xf,y0,yf,z0,zf]
Maxiter=500
tol=1e-2
u,x,y,z,maxerr,avgrerr=Helmholz(f,g,bx0,bxf,by0,byf,bz0,bzf,D,Mx,My,Mz,tol,Maxiter)
fig=plt.figure()
ax=fig.gca(projection='3d')
surf=ax.scatter3D(x,y,z,c=u,cmap=cm.coolwarm)
ax.set_xlabel('x',fontsize=20)
ax.set_ylabel('y',fontsize=20)
ax.set_zlabel('z',fontsize=20)
plt.show()