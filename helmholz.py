
#helmholz function
import numpy as np
import copy as cp
def Helmholz(f,g,bx0,bxf,by0,byf,D,Nx,Ny,tol,Maxiter):
    x0=D[0]
    xf=D[1]
    y0=D[2]
    yf=D[3]
    dx=(xf-x0)/Nx
    dy=(yf-y0)/Ny
    x=np.linspace(x0,xf+dx,Nx+1)
    y=np.linspace(y0,yf+dy,Ny+1)
    dx2=dx**2
    dy2=dy**2
    dxy2=2*(dx2+dy2)
    rx=dy2/dxy2
    ry=dx2/dxy2
    rxy=dx2*dy2/dxy2
    NNx=Nx+1
    NNy=Ny+1
    u=np.zeros([NNx,NNy])
    for m in range(0,NNx):
        u[m,0]=by0(x[m])
        u[m,Ny]=byf(x[m])
    for n in range(0,NNy):
        u[0,n]=bx0(y[n])
        u[Nx,n]=bxf(y[n])
    sum=np.sum(np.sum(u[0:Nx,2:NNy]))+np.sum(np.sum(u[1:NNx,0:Ny]))
    mean=sum/(2*((Nx-1)+(Ny-1)))
    u[1:Nx,1:Ny]=mean
    X,Y=np.meshgrid(x,y)
    F=f(X,Y)
    G=g(X,Y)
    maxerr=np.zeros(Maxiter)
    avrgerr=cp.deepcopy(maxerr)
    for itr in range(0,Maxiter):
        for i in range(1,Nx):
            for j in range(1,Ny):
                u[i,j]=rx*(u[i+1,j]+u[i-1,j])+ry*(u[i,j+1]+u[i,j-1])+rxy*(G[i,j]*u[i,j]-F[i,j])
        if(itr>0):
            maxerr[itr-1]=np.max(np.max(np.abs(u-u0)))
            avrgerr[itr-1]=(np.mean(np.mean(np.abs(u-u0)))
            if (maxerr[itr-1]<tol):
                break
        u0=cp.deepcopy(u)
    return u,X,Y,maxerr,avrgerr




