import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sqrt as sympy_sqrt

# Parameters
h, v = 10000, 0.99 * 3e8
c, tau = 3e8, 2.2e-6
N0, G, M = 10000, 6.67430e-11, 5.972e24
R = 6.371e6

# GR time dilation factor
r = symbols('r')
phi = -G * M / r
gamma_GR = sympy_sqrt(1 - 2 * phi / (c**2))
gamma_GR_val = float(gamma_GR.subs(r, R + h).evalf())

# SR time dilation factor
gamma_SR = 1 / np.sqrt(1 - (v / c)**2)

# Total effective time
t_eff = h / v / (gamma_SR * gamma_GR_val)

# Decay calculations
N_GR = N0 * np.exp(-t_eff / tau)
N_nonreal = N0 * np.exp(-h / v / tau)

# =========================
# Enhanced Visualization
# =========================

plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(10, 6))

theories = ['General Relativity', 'Without Relativity']
values = [N_GR, N_nonreal]

bars = ax.bar(
    theories,
    values,
    color=['royalblue', 'crimson'],
    edgecolor='white',
    linewidth=1.5
)

# Title
ax.set_title(
    'Muon Decay: Relativistic Effects on Muon Survival',
    fontsize=16,
    fontweight='bold',
    pad=15
)

ax.set_ylabel('Number of Muons Remaining', fontsize=12)
ax.set_xlabel('Theory', fontsize=12)

# Grid
ax.grid(axis='y', linestyle='--', alpha=0.4)

# Value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        height + 20,
        f'{height:.1f}',
        ha='center',
        fontsize=11,
        fontweight='bold'
    )

# Difference annotation
difference = abs(N_GR - N_nonreal)

ax.annotate(
    f'Difference = {difference:.1f}',
    xy=(0.5, max(values)),
    xytext=(0.5, max(values) + 120),
    ha='center',
    arrowprops=dict(arrowstyle='->', lw=1.5)
)

# Equation box
ax.text(
    0.02,
    0.95,
    r'$N = N_0 e^{-t/\tau}$',
    transform=ax.transAxes,
    fontsize=12,
    verticalalignment='top',
    bbox=dict(boxstyle='round', facecolor='black', alpha=0.7)
)

plt.xticks(rotation=15)
plt.tight_layout()

plt.savefig(
    'muon_decay_comparison.png',
    dpi=300,
    bbox_inches='tight'
)

plt.show()