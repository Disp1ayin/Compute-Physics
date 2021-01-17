import numpy as np
import copy
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator

dx=1
Nx=100
dy=1
Ny=100
x=np.arange(0,Nx+dx,dx)
y=np.arange(0,Ny+dy,dy)
nx=x.size
ny=y.size
ns=1e5

u=np.zeros([nx,ny])
#initialization
u[nx-1,:]=10
u_old=copy.deepcopy(u)
u_new=copy.deepcopy(u)

