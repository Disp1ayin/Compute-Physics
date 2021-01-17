import numpy as np
import matplotlib.pyplot as plt
from time import time
from scipy.interpolate import lagrange

# 计算时间的初值
n = 7
n_list = range(n)
n_exam = np.linspace(n, n + 1, 2)
time_list = []
time_exam = []
i = 0

# 莱布尼兹方法
for n in n_list:
    flag = True

    time_start = time()
    while flag:
        temp = 4 / (2 * i + 1)
        i += 1
        if temp < 10 ** (-n):
            time_end = time()
            time_list.append(time_end - time_start)

            flag = False
# 插值
n_la = np.linspace(0, 10, 100)
la_result = lagrange(n_list, time_list)

# 验证插值精度
for n in n_exam:
    time_start = time()
    flag = True
    while flag:
        temp = 4 / (2 * i + 1)
        i += 1
        if temp < 10 ** (-n):
            time_end = time()
            time_exam.append(time_end - time_start)

            flag = False

# 绘制图像

plt.plot(n_la, la_result(n_la))
plt.plot(n_list, time_list, '+', c='r')
plt.plot(n_exam, time_exam, 'v', c='m')
plt.xlabel('Digit', fontsize=12)
plt.ylabel('t(s)', fontsize=13)
plt.title('Leibniz Method to Calculate Pi')
plt.xlim(0)
plt.ylim(0)
plt.show()