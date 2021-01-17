from helmholz import  Helmholz
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pylab as plt
f=lambda x,y:x**2+y**2
g=lambda x,y:x**(1/2)
bx0=lambda y:y**2
bxf=lambda y:16*np.cos(y)
by0=lambda x:x**2
byf=lambda x:16*np.cos(x)
x0=0
xf=4
y0=0
yf=4
Mx=100
My=100
D=[x0,xf,y0,yf]
Maxiter=1000
tol=1e-3
u,x,y,maxerr,avgrerr=Helmholz(f,g,bx0,bxf,by0,byf,D,Mx,My,tol,Maxiter)
fig=plt.figure()
ax=fig.gca(projection='3d')
surf=ax.plot_surface(x,y,u,cmap=cm.coolwarm,linewidth=2)
ax.set_xlabel('x',fontsize=20)
ax.set_ylabel('y',fontsize=20)
ax.set_zlabel('z',fontsize=20)
fig.colorbar(surf,shrink=0.5,aspect=5)
plt.show()