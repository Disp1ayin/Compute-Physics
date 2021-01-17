"""三维亥姆霍兹求解
uxx+uyy+uzz+g*u=f
g=sqrt(x), f=x**2+y**2+z**2
0<=x,y,z<=4
u(0,y,z)=y**2+z**2  u(4,y,z)=16cos(yz)
u(x,0,z)=x**2+z**2  u(x,4,z)=16cos(xz)
u(x,y,0)=x**2+y**2  u(x,y,4)=16cos(xy)"""
from Helmholtz_3d import Helmholtz_3d
import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D


# define function f&g
f = lambda x, y, z: x ** 2 + y ** 2 + z ** 2
g = lambda x, y, z: (x) ** (1 / 2)

# define calculating domain
x0 = 0
xf = 4
y0 = 0
yf = 4
z0 = 0
zf = 4

# Numbers of elements
Mx = 20
My = 20
Mz = 20

# boundary
bx0 = lambda y, z: y ** 2 + z ** 2
bxf = lambda y, z: 16 * np.cos(y*z)
by0 = lambda x, z: x ** 2 + z ** 2
byf = lambda x, z: 16 * np.cos(x*z)
bz0 = lambda x, y: x ** 2 + y ** 2
bzf = lambda x, y: 16 * np.cos(x*y)

# condition
D = [x0, xf, y0, yf, z0, zf]
MaxIter = 1000
tol = 1e-6

# solving
u, x, y, z, maxerr, meanerr = Helmholtz_3d(f, g, bx0, bxf, by0, byf, bz0, bzf, D, Mx, My, Mz, tol, MaxIter)

# Plot the surface.
fig = plt.figure()
ax = fig.gca(projection='3d')
sc = ax.scatter(x, y, z, c=u, alpha=0.5, cmap='coolwarm')
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_ylabel('z', fontsize=14)
# Add a color bar which maps values to colors.
fig.colorbar(sc, shrink=0.5, aspect=5)
plt.show()
