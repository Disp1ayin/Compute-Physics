import numpy as np
def F(y,t,G=1,M=1,m=1):
    # Use a breakpoint in the code line below to debug your script.
    r=np.sqrt(y[0]**2+y[1]**2)
    k=-G*M*m
    dy=[0,0,0,0]
    dy[0]=y[2]
    dy[1]=y[3]
    dy[2]=k*y[0]/(r**3)
    dy[3]=k*y[1]/(r**3)
    return dy