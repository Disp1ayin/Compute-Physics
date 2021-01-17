import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import  Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator

#heat conduction equation
fig=plt.figure()
ax=fig.gca(projection='3d')

dx=0.02
l=1
x=np.arange(0,l+dx,dx)
a2=2;
dt=0.01;
c=a2*(dt**2)/(dx**2);
nx=x.size
nt=50;
u=np.zeros([nx,nt])
X,Y=np.meshgrid(np.arange(0,nt),x)
#initialization


u[0,:]=0;
u[nx-1,:]=0;
for i in np.arange(0,nx):
    tempx=i*dx
    if(tempx>=3*l/7 and tempx<=4*l/7):
        u[i,0]=np.sin(7*np.pi*tempx/l)
        continue
    else:
        u[i,0]=0

#solve
for k in range(0,nt-1):
    u[1:nx-1,k+1]=c*(u[2:nx,k]+u[0:nx-2,k])+2*(1-c)*u[1:nx-1,k]-u[1:nx-1,k-1]

#plot
surf=ax.plot_surface(X,Y,u,cmap=cm.coolwarm,linewidth=2)
surf.antialiased=False

ax.set_xlabel('t',fontsize=10);
ax.set_ylabel('x',fontsize=10);
ax.set_zlabel('u',fontsize=10);
ax.zaxis.set_major_locator(LinearLocator(10))
fig.colorbar(surf,shrink=0.5,aspect=10)
plt.show()