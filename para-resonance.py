#弹簧摆的参数共振模拟
import numpy as np
from  scipy.integrate import odeint
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sympy

def F(y,t,omiga,pendulum_omiga,l):
    dy=np.zeros(2)
    dy[0]=y[1]
    l=l;
    dl = g / (omiga ** 2) # 压缩长度
    dlfun=dl*np.cos(omiga*t)
    dy[1]=-(pendulum_omiga**2)*(1+dlfun/l)*y[0]
    return dy

#初始参数设置
g=9.8;#重力加速度
l=1;#摆长
pendulum_omiga=(g/l)**0.5;
x=sympy.symbols("x")
l_max=sympy.solveset(sympy.Eq((1+4*l)*x**2+(8*l-4*l**2)*x-16*l**2,0),x,domain=sympy.S.Reals)

omiga0=2*pendulum_omiga;#弹簧振动频率
dl0=(1/4)*l

domiga=pendulum_omiga*dl0/(2*l)#弹簧频率改变范围
y0=[np.pi/16,0]#初始值
t_start=0
t_end=60
dt=0.02
t=np.arange(t_start,t_end+dt,dt)
#绘图
fig=plt.figure()
ax=fig.gca()
result0=odeint(F,y0,t,args=(omiga0,pendulum_omiga,l))
plotpattern,=ax.plot(t,result0[:,0],linewidth=2)
ax.set(xlim=(t_start,t_end),ylim=(-np.pi,np.pi),xlabel='time',ylabel='angle')


#slider
axcolor = 'lightgoldenrodyellow'  # slider的颜色
pos= plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor) # slider的位置
slider_omiga=Slider(pos,'/$omiga$',omiga0-domiga,omiga0+domiga,valinit=omiga0)
def update(val):
    somiga=slider_omiga.val
    result = odeint(F, y0, t, args=(somiga, pendulum_omiga,l))
    plotpattern.set_xdata(t)
    plotpattern.set_ydata(result[:,0])
    fig.canvas.draw_idle()

slider_omiga.on_changed(update)
#图2，动画
fig2=plt.figure(2)

ax2=fig2.gca()
celling,=ax2.plot([-1,1],[0,0])
line,=ax2.plot([0,0 ],[ 0,0],'-o')

xdata=[(l+dl0*np.cos(omiga0*t[i]))*np.sin(result0[i,0]) for i in range(len(t))]
ydata=[-(l+dl0*np.cos(omiga0*t[i]))*np.cos(result0[i,0]) for i in range(len(t))]
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1.8,1)
    time_text.set_text('')
    return line, time_text

def update_line(i):
    newx=[0,xdata[i]]
    newy=[0,ydata[i]]
    line.set_data(newx,newy)
    time_text.set_text(time_template % (0.1 * i))
    return line,time_text


ani=animation.FuncAnimation(fig2,update_line,range(1,len(xdata)),init_func=init,interval=50)
ani.save('parameter resonance.gif', writer='imagemagick', fps=60)



#Done!
plt.show()


