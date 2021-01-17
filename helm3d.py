import numpy as np
import copy as cp
def Helmholz(f,g,bx0,bxf,by0,byf,bz0,bzf,D,Nx,Ny,Nz,tol,Maxiter):
    x0 = D[0]
    xf=D[1]
    y0 = D[2]
    yf = D[3]
    z0 = D[4]
    zf = D[5]
    dx=(xf-x0)/Nx
    dy = (yf - y0) / Ny
    dz = (zf - z0) / Nz
    x=np.linspace(x0,xf+dx,Nx+1)
    y= np.linspace(y0, yf + dy, Ny + 1)
    z = np.linspace(z0, zf + dz, Nz + 1)
    X,Y,Z=np.meshgrid(x,y,z)
    F=f(X,Y,Z)
    G=g(X,Y,Z)
    dx2=dx**2
    dy2=dy**2
    dz2=dz**2
    dxyz2=2*(dy2*dz2+dx2*dy2*dx2*dz2)
    rx=dy2*dz2/dxyz2
    ry=dx2*dz2/dxyz2
    rz=dx2*dy2/dxyz2
    rxyz=dx2*dy2*dz2/dxyz2
    NNx=Nx+1
    NNy=Ny+1
    NNz=Nz+1
    u=np.zeros([NNx,NNy,NNz])
    print('preparation done')
    #边界条件

    for i in range(0,NNx):
        for j in range(0,NNy):
            u[i,j,0]=bz0(x[i],y[j])
    for i in range(0, NNx):
        for j in range(0, NNy):
            u[i, j, Nz] = bzf(x[i], y[j])
    for i in range(0,NNx):
        for k in range(0,NNz):
            u[i,0,k]=by0(x[i],z[k])
    for i in range(0,NNx):
        for k in range(0,NNz):
            u[i,Ny,k]=byf(x[i],z[k])
    for j in range(0,NNy):
        for k in range(0,NNz):
            u[0,j,k]=bx0(y[j],z[k])
    for j in range(0, NNy):
        for k in range(0, NNz):
            u[Nx, j, k] = bxf(y[j], z[k])

    print('boundry conduction done')

    #用平均值初始化
    sum = np.sum(np.sum(u[0:NNx, 0:NNy,0:NNz]))
    mean = sum / (1* ((Nx - 1) + (Ny - 1)+(Nz-1)))
    u[1:Nx, 1:Ny,1:Nz] = mean
    print('initialization done')
    #误差数列
    maxerr = np.zeros(Maxiter)
    avrgerr = cp.deepcopy(maxerr)
    #求解
    for itr in range(0,Maxiter):
        for i in range(1,Nx):
            for j in range(1,Ny):
                for k in range(1,Nz):
                    u[i,j,k]=rx*(u[i+1,j,k]+u[i-1,j,k])+ry*(u[i,j+1,k]+u[i,j-1,k])+rz*(u[i,j,k+1]+u[i,j,k-1])+rxyz*(G[i,j,k]*u[i,j,k]-F[i,j,k])


        if (itr>0):
            maxerr[itr-1]=np.max(np.max(np.abs(u-u0)))
            avrgerr[itr - 1] = np.mean(np.mean(np.abs(u - u0)))
            if (maxerr[itr-1]<tol):
                break
        u0=cp.deepcopy(u)

    print('solve done')

    return u,X,Y,Z,maxerr,avrgerr



