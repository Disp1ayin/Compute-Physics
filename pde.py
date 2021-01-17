import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import  Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator

#heat conduction equation
fig=plt.figure()
ax=fig.gca(projection='3d')

dx=1
Nx=20
x=np.arange(0,Nx+dx,dx)
a2=10;
dt=0.01;
r=a2*dt/(dx**2);
nx=x.size
nt=50;
u=np.zeros([nx,nt])
X,Y=np.meshgrid(np.arange(0,nt),x)
u[10:12,0]=1
for k in range(0,nt-1):
    u[1:nx-1,k+1]=(1-2*r)*u[1:nx-1,k]+r*(u[2:nx,k]+u[0:nx-2,k])

#plot
surf=ax.plot_surface(X,Y,u,cmap=cm.coolwarm,linewidth=2)
surf.antialiased=False

ax.set_xlabel('t',fontsize=10);
ax.set_ylabel('x',fontsize=10);
ax.set_zlabel('tempeture',fontsize=10);
ax.set_zlim(0.01,1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
fig.colorbar(surf,shrink=0.5,aspect=10)
plt.show()

