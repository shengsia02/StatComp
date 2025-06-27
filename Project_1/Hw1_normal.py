import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')
fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(10, 8))
plt.suptitle('Normal Distributions', fontsize=18, fontweight='bold')

# 设置全局的 y 轴标签
fig.text(-0.02, 0.5, 'Density', va='center', rotation='vertical', fontsize=15, color='black', fontweight='bold')

# Plot 1
xlim1 = [-15, 15]
mu1 = 0
s_values = np.arange(1, 6)
x1 = np.linspace(xlim1[0], xlim1[1], 1000)
ax0.axis([xlim1[0], xlim1[1], -0.02, 0.43])
ax0.set_yticks(np.arange(0, 0.41, 0.1))
ax0.tick_params(axis='both', colors='black')

# Plot 2
xlim2 = [-3, 7]
mu_values = np.arange(0, 5)
s2 = 1
x2 = np.linspace(xlim2[0], xlim2[1], 1000)
ax1.axis([xlim2[0], xlim2[1], -0.02, 0.45])
ax1.set_xticks(np.arange(-2, 7, 2))
ax1.set_yticks(np.arange(0, 0.41, 0.1))
ax1.tick_params(axis='both', colors='black')

# 初始化图形
lines0 = [ax0.plot([], [], linewidth=3, label=f"$\sigma$ = {pr}")[0] for pr in s_values]
lines1 = [ax1.plot([], [], linewidth=3, label=f"$\mu$ = {pr}")[0] for pr in mu_values]

def init():
    for line in lines0 + lines1:
        line.set_data([], [])
    return lines0 + lines1

def update(frame):
    # 更新 ax0 的线条
    if frame < len(s_values):
        y0 = norm.pdf(x1, mu1, s_values[frame])
        lines0[frame].set_data(x1, y0)
    
    # 更新 ax1 的线条
    if frame < len(mu_values):
        y1 = norm.pdf(x2, mu_values[frame], s2)
        lines1[frame].set_data(x2, y1)
    
    return lines0 + lines1

ani = FuncAnimation(fig, update, frames=max(len(s_values), len(mu_values)), init_func=init, blit=True, repeat=False, interval=500)

ax0.legend(bbox_to_anchor=(1.2, 1))
ax1.legend(bbox_to_anchor=(1.2, 1))

plt.tight_layout()
plt.show()