# 目的：练习绘图
# 作者：王飞鸿

import matplotlib.pyplot as plt

# 建立画板
# fig = plt.figure()
# 建立坐标轴
'''
ax = fig.add_subplot(111)
ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title="An Example Axes",
       ylabel="Y-Axis", xlabel="X-Axis")
ax1 = fig.add_subplot(221)
# ax2 = fig.add_subplot(222)
# ax3 = fig.add_subplot(223)
'''
# Multiple Axes 一次性生成所有axes
fig1 = plt.figure()
fig1, axes = plt.subplot(nrow=2, ncols=2)
axes[0,0].set(title='Upper Left')
axes[0,1].set(title='Upper Right')
axes[1,0].set(title='Lower Left')
axes[1,1].set(title='Lower Right')
plt.plot([1, 2, 3, 4],[10,20 ,25,30],color='lightblue', linewidth=3)
plt.xlim(0.5, 4.5)

plt.show()
