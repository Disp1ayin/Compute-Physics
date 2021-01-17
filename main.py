import numpy as np
from  scipy.integrate import odeint
import matplotlib.pyplot as plt
from func import F
from matplotlib.patches import Circle
from matplotlib.widgets import Slider
# This is a sample Python script.



#参数设置
close_dist=5
G=1
M=10
m=1
#求解运动方程

def solve_orbit(l):
    t_min = 0
    t_max = 100
    dt = 0.1
    v0 = l / close_dist
    t = np.arange(t_min, t_max + dt, dt)
    y0 = (close_dist, 0, 0, v0)
    result = odeint(F, y0, t, args=(G, M, m))
    return result





#绘图
fig=plt.figure(figsize=(30,20))

#plt.title('Orbit')
#E>0
ax1=fig.add_subplot(2,2,1)
t_min = 0
t_max = 10
dt = 0.1
v0 =20/close_dist
t = np.arange(t_min, t_max + dt, dt)
y0 = (5, 0, 0, v0)
result1 = odeint(F, y0, t, args=(G, M, m))
ax1.plot(result1[:,0],result1[:,1],c='b',linewidth=2)
ax1.plot(result1[:,0],-result1[:,1],c='b',linewidth=2)
ax1.set(xlabel='x',ylabel='y',title='E>0',xlim=(-1,5))


#E=0
ax2=fig.add_subplot(2,2,2)
result2=solve_orbit(10)
ax2.plot(result2[:,0],result2[:,1],c='b',linewidth=2)
ax2.plot(result2[:,0],-result2[:,1],c='b',linewidth=2)
ax2.add_artist(Circle((0,0),0.35))
ax2.set(xlabel='x',ylabel='y',title='E=0')
#E<0
ax3=fig.add_subplot(2,2,3)
result3=solve_orbit(5)
ax3.plot(result3[:,0],result3[:,1],linewidth=2)
ax3.add_artist(Circle((0,0),0.1))
ax3.set(xlabel='x',ylabel='y')
ax3.set_title('E<0',fontsize=10)



#slider part
ax4=fig.add_subplot(2,2,4)
result4=solve_orbit(5)
li,=ax4.plot(result4[:,0],result4[:,1],linewidth=2)
ax4.add_artist(Circle((0,0),0.1))
ax4.set(title='Slider',xlim=(-10,5),ylim=(-20,20))

#Slider
axcolor = 'lightgoldenrodyellow'  # slider的颜色
s_pos=fig.add_axes([0.25, 0.03, 0.65, 0.03], facecolor=axcolor)

sl=Slider(s_pos,'auglar momentum',0.25,9,valinit=1)
def update(val):
    l=sl.val
    result=solve_orbit(l)
    li.set_xdata(result[:,0])
    li.set_ydata(result[:,1])
    fig.canvas.draw_idle()

sl.on_changed(update)

#final
plt.subplots_adjust(wspace =0.5, hspace =0.5)#调整子图间距
plt.show()



