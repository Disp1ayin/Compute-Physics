import numpy as np
import copy as cp


def Helmholtz_3d(f, g, bx0, bxf, by0, byf, bz0, bzf, D, Nx, Ny, Nz, tol, MaxIter):
    # Total domain defined
    x0 = D[0]
    xf = D[1]
    y0 = D[2]
    yf = D[3]
    z0 = D[4]
    zf = D[5]

    # coordinates vectors
    dx = (xf - x0) / Nx
    x = np.linspace(x0, x0 + Nx * dx, Nx + 1)
    dy = (yf - y0) / Ny
    y = np.linspace(y0, y0 + Ny * dy, Ny + 1)
    dz = (zf - z0) / Nz
    z = np.linspace(z0, z0 + Nz * dx, Nz + 1)

    # coefficient
    dx2 = dx * dx
    dy2 = dy * dy
    dz2 = dz * dz
    dxyz2 = 2 * (dx2 * dy2 + dy2 * dz2 + dx2 * dz2)
    rx = dy2 * dz2 / dxyz2
    ry = dx2 * dz2 / dxyz2
    rz = dx2 * dy2 / dxyz2
    rxyz = rx * dx2

    # Number of nodes
    NNx = Nx + 1
    NNy = Ny + 1
    NNz = Nz + 1
    u = np.zeros([NNz, NNy, NNx])
    # Boundary values
    # x
    for m in range(0, NNy):
        for n in range(0, NNz):
            u[n, m, 0] = bx0(y[m], z[n])
            u[n, m, Nx] = bxf(y[m], z[n])
    # y
    for m in range(0, NNx):
        for n in range(0, NNz):
            u[n, 0, m] = by0(x[m], z[n])
            u[n, Ny, m] = byf(x[m], z[n])
    # z
    for m in range(0, NNy):
        for n in range(0, NNx):
            u[0, m, n] = bz0(x[m], y[n])
            u[Nz, m, n] = bzf(x[m], y[n])
    # Set mean of boundary values as the initial iteration
    sum_of_bv = np.sum(np.sum(u[0:-1, 0:-1, 0:-1]))
    mean_of_bv = sum_of_bv / (2 * ((Nx - 1) + (Ny - 1) + (Nz - 1)))
    u[1:Nz, 1:Ny, 1:Nx] = mean_of_bv
    print('initialization')

    # Calculating f&g
    X, Y, Z = np.meshgrid(x, y, z)
    F = f(X, Y, Z)
    G = g(X, Y, Z)
    print(' ')

    print('Calculating f&g')

    # Calculation
    print(' ')
    print(' Solving')
    maxerr = np.zeros(MaxIter)
    avrgerr = cp.deepcopy(maxerr)
    for itr in range(0, MaxIter):
        u[1:-1, 1:-1, 1:-1] = rx * (u[1:-1, 1:-1, 2:] + u[1:-1, 1:-1, :-2]) + ry * (
                    u[1:-1, 2:, 1:-1] + u[1:-1, :-2, 1:-1]) \
                              + rz * (u[2:, 1:-1, 1:-1] + u[:-2, 1:-1, 1:-1]) + rxyz * (G[1:-1, 1:-1, 1:-1] * u[1:-1, 1:-1, 1:-1] -
                                                                                        F[1:-1, 1:-1, 1:-1])
        if (itr > 0):
            maxerr[itr - 1] = np.max(np.max(np.abs(u - u0)))
            avrgerr[itr - 1] = np.mean(np.mean(np.abs(u - u0)))
            if (np.max(np.max(np.abs(u - u0))) < tol):
                break
        u0 = cp.deepcopy(u)

    return u, X, Y, Z, maxerr, avrgerr
