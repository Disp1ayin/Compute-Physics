
import matplotlib.pyplot as plt

from matplotlib.widgets import Slider,RadioButtons
import numpy as np
def funt(omiga1,omiga2):
    x=np.linspace(-5*np.pi,5*np.pi,200)
    y1=np.sin(omiga1*x)
    y2=np.cos(omiga2*x)
    return(x,y1+y2)
fig,ax=plt.subplots()
plt.subplots_adjust(bottom=0.2,left=0.3)
x,y=funt(2,3)
result,=plt.plot(x,y,c='blue')
axcolor = 'lightgoldenrodyellow'  # slider的颜色
om1= plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor) # 第一slider的位置
om2 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
som1=Slider(om1,r'$omiga_1$',0.5,10,valinit=3)
som2=Slider(om2,r'$omiga_2$',0.5,10,valinit=5)


def update(val):
    s1=som1.val
    s2=som2.val
    x,y=funt(s1,s2)
    result.set_xdata(x)
    result.set_ydata(y)
    fig.canvas.draw_idle()

som1.on_changed(update)
som2.on_changed(update)



cc = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(cc, ('red', 'blue', 'green'), active=0)


def colorfunc(label):
    result.set_color(label)
    fig.canvas.draw_idle()


radio.on_clicked(colorfunc)
plt.show()
