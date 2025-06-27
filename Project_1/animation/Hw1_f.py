import numpy as np
from scipy.stats import f
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize = (8, 6))
xlim = [0, 2]
x = np.linspace(xlim[0], xlim[1], 1000)

# n1、n2 互換差別不大，其中一個值固定，另一個值變得超大，越集中，且越來越接近不偏
n1 = 750
n2 = np.arange(150, 1501, 50)
colors = plt.colormaps['twilight'](np.linspace(0.3, 0.9, len(n2))) # 定义颜色列表

# fix xlim before animation
# ax.axis([xlim[0], xlim[1], 0, 0.4])
plt.xlabel('x', fontsize = 18, color = 'black', fontweight = 'bold')
plt.ylabel('Density', fontsize = 18, color = 'black', fontweight = 'bold')
plt.title(r'$F$ Distributions', fontsize = 20, fontweight = 'bold')

for pr, color in zip(n2, colors):
    y = f.pdf(x, dfn = n1, dfd = pr)
    line, = ax.plot(x, y, lw = 1.8, color = color, alpha = 0.8, label = r'$n_1$ = {}, $n_2$ = {}'.format(n1, pr))
    ax.legend([line], [line.get_label()], loc = 'upper right')
    ax.tick_params(axis = 'both', colors = 'black')
    ax.set_xlim([0.5, 1.5])
    ax.set_ylim([0, 7.5])
    ax.set_yticks(np.arange(0, 7.5, 1))
    plt.tight_layout()
    plt.pause(0.5)

    # 清除之前的图例
    if ax.get_legend() is not None:
        ax.get_legend().remove()
    
ax.text(0.8, 6.7, '$n_1 = {},\ {} \leq n_2 \leq {}$'.format(n1, n2[0], n2[-1]), fontsize = 15, color = 'black')
plt.show()