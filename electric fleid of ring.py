# 带电圆环电势与电场
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt
from numpy import cos, sin, pi, vectorize, linspace, mgrid, zeros, gradient
from scipy.integrate import quad
from mpl_toolkits.mplot3d import Axes3D

# 缺省参数
k = 1e-7
N = 10
# 角度
theta = linspace(0, 2 * pi, 20)
# 电势微分形式(R为场点到原点距离在xy平面投影，r为圆环半径)
dp = lambda theta, R, h, r: 1 / (R ** 2 + r ** 2 + h ** 2 - 2 * R * r * cos(theta)) ** 0.5


# 装饰器(?)
@vectorize
# 电势积分
def potential(R, h, r):
    p = quad(dp, 0, 2 * pi, args=(R, h, r))[0]
    return p


# 电场
def get_field(p):
    [Ex, Ey, Ez] = gradient(-p)
    return Ex, Ey, Ez


# 数据
def get_data(q, r, Lx=6, Ly=6, Lz=6, N=N):
    x, y, z = mgrid[-Lx:Lx:N * 1j, -Ly:Ly:N * 1j, -Lz:Lz:N * 1j]
    x2, y2 = mgrid[-Lx:Lx:N * 1j, -Ly:Ly:N * 1j]
    z2 = linspace(-Lz, Lz, N)
    R = (x ** 2 + y ** 2) ** 0.5
    p = potential(R, z, r)
    Ex, Ey, Ez = get_field(p)
    return x, y, z, q * k * p, q * k * Ex, q * k * Ey, q * k * Ez, x2, y2, z2


# 绘图函数
def plot(ax, ax2, q, r):
    surf = zeros([N, N]);
    data = get_data(q=q, r=r)
    X, Y, Z, P, U, V, W, x2, y2, z2 = data
    ax.quiver(X, Y, Z, U, V, W, normalize=True)
    ax.plot(r * cos(theta), r * sin(theta), zeros(theta.shape[0]), color='crimson', linewidth=4)
    ax2.plot(r * cos(theta), r * sin(theta), zeros(theta.shape[0]), color='crimson', linewidth=4)
    pot = 8;
    for i in range(N):
        for j in range(N):
            for k in range(N):

                if (P[i, j, k] * (10 ** 8) - pot) > 0.1:
                    surf[i, j] = z2[k];

    ax2.plot_surface(x2, y2, surf)


# 绘图

fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(2, 1, 1, projection='3d')
ax2 = fig.add_subplot(2, 1, 2, projection='3d')

plot(ax, ax2, q=1, r=3)
plt.show()