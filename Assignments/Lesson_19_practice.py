#Lesson_19_practice

import matplotlib.pyplot as plt
import numpy as np


colors = plt.rcParams['axes.prop_cycle'].by_key()['color']


#Anscombe Quartet.
def linear(x,a):
    '''A linear fitting function.'''
    return a[0] + a[1]*x

def χ2(Y,y):
    '''Unscaled χ^2'''
    return np.sum((Y-y)**2)

anscombe = np.array([[10.0,8.04,10.0,9.14,10.0,7.46,8.0,6.58],[8.0,6.95,8.0,8.14,8.0,6.77,8.0,5.76],
[13.0,7.58,13.0,8.74,13.0,12.74,8.0,7.71],[9.0,8.81,9.0,8.77,9.0,7.11,8.0,8.84],
[11.0,8.33,11.0,9.26,11.0,7.81,8.0,8.47],[14.0,9.96,14.0,8.10,14.0,8.84,8.0,7.04],
[6.0,7.24,6.0,6.13,6.0,6.08,8.0,5.25],[4.0,4.26,4.0,3.10,4.0,5.39,19.0,12.50],
[12.0,10.84,12.0,9.13,12.0,8.15,8.0,5.56],[7.0,4.82,7.0,7.26,7.0,6.42,8.0,7.91],
[5.0,5.68,5.0,4.74,5.0,5.73,8.0,6.8]])

fig, axes = plt.subplots(2,2,sharex=True, sharey=True, squeeze=False, figsize=(10,7))
plt.subplots_adjust(hspace=0.05,wspace=0.05)
x = np.linspace(4,20,1000)
for i, ax in enumerate(axes.flat):
    Y = linear(x,(3,0.5))
    ax.plot(x,Y,'-',color=colors[0], linewidth=2, label='y = 0.5x + 3')
    r2 = χ2(linear(anscombe[:,2*i],(3,0.5)),anscombe[:,2*i+1])
    ax.plot(anscombe[:,2*i],anscombe[:,2*i+1],'o', markeredgecolor='None', alpha=0.7, markersize=7,
           label=f'$\chi^2 = {r2:4.2f}$', mfc=colors[2])
    ax.legend(loc='lower right')

[ax.set_ylabel('y') for ax in axes[:,0]]
[ax.set_xlabel('x') for ax in axes[-1,:]]

plt.show()





# Challenge is load the experimental data for rod_temperature.dat and perform a linear fit to the data
# and display the resulting fit function and parameters in the legend.

def Σ(σ, q):
    '''Compute the Σ function needed for linear fits.'''
    return np.sum(q / σ**2)


def get_a(x, y, σ):
    '''Get the χ² best-fit values of a0 and a1 for a linear model.'''
    Σy = Σ(σ, y)
    Σx = Σ(σ, x)
    Σx2 = Σ(σ, x**2)
    Σ1 = Σ(σ, np.ones_like(x))
    Σxy = Σ(σ, x * y)

    D = Σ1 * Σx2 - Σx**2
    a = np.array([
        Σy * Σx2 - Σx * Σxy,
        Σ1 * Σxy - Σx * Σy,
    ]) / D

    aErr = np.array([
        np.sqrt(Σx2 / D),
        np.sqrt(Σ1 / D),
    ])

    return a, aErr


# Use a path relative to this file so the data loads reliably from any working directory.
from pathlib import Path

data_path = Path(__file__).resolve().parents[2] / 'data' / 'rod_temperature.dat'
x, y, σ = np.loadtxt(data_path, unpack=True)

plt.errorbar(x, y, yerr=σ, linestyle='None', marker='o', capsize=0, elinewidth=1.5)

a, aErr = get_a(x, y, σ)

plt.plot(x, linear(x, a), label='fit', zorder=0)

plt.xlabel('L (cm)')
plt.ylabel('Temperature (K)')
plt.xlim(0,10)
plt.legend(loc=2)
plt.show()

