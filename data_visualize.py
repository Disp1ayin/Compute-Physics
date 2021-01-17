# 数据可视化
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import math
from matplotlib.patches import Circle

# 画布
fig = plt.figure(figsize=((30, 20)))

# Part1 一维函数可视化
ax1 = fig.add_subplot(2, 2, 1)
x = np.arange(0.0, 2.0, 0.01)
y = np.sin(2 * x ** 2) * np.cos(x ** 3)
ax1.plot(x, y)
ax1.set(xlabel='x', ylabel='y', title=' $\sin(2x^2)*cos(x^3)$')
ax1.grid()

# Part2 二维函数可视化
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
ax2.set(xlabel='x', ylabel='y', zlabel='values')
ax2.set_title(' $\sin(xy)*cos(xy)$')
X, Y = np.meshgrid(np.arange(-2 * np.pi, 2 * np.pi, .2), np.arange(-2 * np.pi, 2 * np.pi, .2))
Z = np.sin(X * Y / 10) * np.cos(X * Y / 10)
surf = ax2.plot_surface(X, Y, Z)
fig.colorbar(surf, shrink=0.5, aspect=2)


# Part3 三维函数可视化
def randrange(n, min_v, max_v):
    return (max_v - min_v) * np.random.rand(n) + min_v


n = 100
ax3 = fig.add_subplot(2, 2, 3, projection='3d')
ax3.set(xlabel='x', ylabel='y', zlabel='z')
x = randrange(n, -5, 5)
y = randrange(n, -5, 5)
z = randrange(n, -5, 5)
d = np.sin(np.sqrt(x ** 2 + y ** 2 + z ** 2))
ax3.scatter3D(x, y, z, c=d, cmap='rainbow')
fig.colorbar(surf, shrink=0.5, aspect=2)
plt.title("$\sin\sqrt{x^2+y^2+z^2}$")
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z')

# Part4 矢量函数可视化(电场)
a = 1
ax4 = fig.add_subplot(2, 2, 4, projection='3d')
x, y, z = np.meshgrid(np.arange(-5, 5, 1), np.arange(-5, 5, 1), np.arange(-5, 5, 1))
p1 = 1 / (x ** 2 + y ** 2 + (z - a) ** 2) * 0.5
p2 = 1 / (x ** 2 + y ** 2 + (z + a) ** 2) * 0.5
p = p1 + p2
[Ex, Ey, Ez] = np.gradient(-p)
ax4.quiver(x, y, z, Ex, Ey, Ez, normalize=True)

fig.colorbar(surf, shrink=0.5, aspect=2)
plt.show()