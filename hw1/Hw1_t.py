import numpy as np
from scipy.stats import t, norm
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize = (8, 6))

xlim = [-6, 6]
x1 = np.linspace(xlim[0], xlim[1], 1000)
df1 = np.arange(0.1, 1.1, 0.1)
df2 = np.arange(3, 31, 3) # t 分佈自由度 >= 30 時，t 分佈近似於標準正態分佈
df3 = np.arange(33, 61, 3)  # 觀察自由度大於 30 後的樣子
dfs = np.concatenate((df1, df2, df3))
# dfs = np.append(df1, df2)

# 定义颜色列表
colors = plt.colormaps['YlGnBu'](np.linspace(0.3, 1, len(dfs)))

# fix xlim before animation
ax.axis([xlim[0], xlim[1], 0, 0.4])

for df, color in zip(dfs, colors):
    y1 = t.pdf(x1, df)
    line, = ax.plot(x1, y1, linewidth = 2, color = color, label = r'$\nu$ = {}'.format(round(df, 2)))
    ax.legend([line], [line.get_label()], loc = 'upper right')
    ax.tick_params(axis = 'both', colors = 'black')
    ax.set_title('$T$ Distributions', fontsize = 18, fontweight = 'bold')
    ax.set_xlabel('x', fontsize = 15, color = 'black', fontweight = 'bold')
    ax.set_ylabel('Density', fontsize = 15, color = 'black', fontweight = 'bold')
    ax.set_ylim([0, 0.41])
    ax.set_yticks(np.arange(0, 0.41, 0.1))
    plt.tight_layout()
    plt.pause(0.5)

    # 清除之前的图例
    if ax.get_legend() is not None:
        ax.get_legend().remove()

x2 = np.linspace(xlim[0], xlim[1], 1000)
y2 = norm.pdf(x2, loc = 0, scale = 1)
line2, = ax.plot(x2, y2, color = 'red', linewidth = 2.5, label = 'Z Distribution')
ax.legend([line2], [line2.get_label()], loc = 'upper right')

plt.text(4, 0.25, r'${} \leq d.f. \leq {}$'.format(dfs[0], dfs[-1]), fontsize = 15, color = 'k', 
         ha = 'center')
plt.show()