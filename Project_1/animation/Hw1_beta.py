import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize = (7, 5))

xlim = [0, 1]
x = np.linspace(xlim[0], xlim[1], 1000)
a = 9
b = np.arange(1, 31, 1)

# 定义颜色列表
colors = plt.colormaps['Oranges'](np.linspace(0.3, 1, len(b)))

# fix xlim before animation
ax.axis([xlim[0], xlim[1], 0, 8.8])

for b1, color in zip(b, colors):
    y = beta.pdf(x, a = a, b = b1)
    line, = ax.plot(x, y, linewidth = 1.5, color = color, label = r'$\alpha$ = {}, $\beta$ = {}'.format(a, b1))
    ax.legend([line], [line.get_label()], loc = 'upper right')
    ax.tick_params(axis = 'both', colors = 'black')
    ax.set_title(r'$\beta$ Distributions', fontsize = 18, fontweight = 'bold')
    ax.set_xlabel('x', fontsize = 15, color = 'black', fontweight = 'bold')
    ax.set_ylabel('Density', fontsize = 15, color = 'black', fontweight = 'bold')
    ax.set_ylim([0, 8.8])
    ax.set_xticks(np.arange(0.2, 1.2, 0.2))
    ax.set_yticks(np.arange(0, 9, 2))
    plt.tight_layout()
    plt.pause(0.5)

    # 清除之前的图例
    if ax.get_legend() is not None:
        ax.get_legend().remove()

plt.text(0.5, 6.5, r'$\alpha = {}$, ${} \leq \beta \leq {}$'.format(a, b[0], b[-1]), fontsize = 15, color = 'k', 
         ha = 'center')
plt.tight_layout()
plt.show()