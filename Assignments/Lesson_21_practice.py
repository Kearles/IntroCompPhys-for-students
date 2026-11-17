#Lesson_21_practice

import numpy as np
import matplotlib.pyplot as plt

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']




from scipy.constants import pi as π
def fourier_transform(y):
    '''Return the discrete Fourier transform of y.'''
    N = y.size
    ŷ = np.zeros([N],dtype=complex)

    return ŷ

# the time series
Δt = 0.1
t = np.arange(0.0,50.0,Δt)
N = t.size
ωₒ = 2.0*π*(0.2)
ϕ = 0.5*π
y = np.sin(ωₒ*t + ϕ) + np.sin(2*ωₒ*t)

# Plot the time series
fig,ax = plt.subplots(1,2, figsize=(8,4))
fig.subplots_adjust(wspace=0.4)

ax[0].plot(t,y)
ax[0].set_xlabel('Time [s]')
ax[0].set_ylabel('Amplitude [arb.]')

# Get the discrete FT
ω = 2*π*np.arange(0,N)/(N*Δt)
ŷ = fourier_transform(y)

# Plot the real and imaginary parts of the DFT
ax[1].plot(ω,ŷ.real,label='real.', color=colors[0])
ax[1].plot(ω,ŷ.imag,linestyle='--',label='imag.', color=colors[-2])

ax[1].set_xlabel('Frequency [rad/s]')
ax[1].set_ylabel('Transform [arb.]')
ax[1].legend(loc='lower right')
plt.show()

#Analying for pervious time series in discrete case.
plt.plot(ω,np.abs(ŷ),color=colors[2])
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Power [arb]')
plt.show()

#More Fourier transform

t,*y = np.loadtxt('../../data/signal.dat',unpack=True)
fig, axes = plt.subplots(1,2,sharex=True, sharey=True, squeeze=True, figsize=(8,4))
fig.subplots_adjust(wspace=0.1)

for i,ax in enumerate(axes):
    ax.plot(t,y[i],'-',color=colors[i], linewidth=1)

axes[0].set_ylabel('y')
[ax.set_xlabel('t') for ax in axes]

ω = 2*π*np.arange(0,t.size)/(t.size*(t[1]-t[0]))

fig, axes = plt.subplots(1,2,sharex=True, sharey=True, squeeze=True, figsize=(8,4))
fig.subplots_adjust(wspace=0.1)

for i,ax in enumerate(axes):
    ŷ = fourier_transform(y[i])
    ax.plot(ω,np.abs(ŷ),color=colors[i], linewidth=1)
    ax.set_xlabel('ω')
    ax.set_xlim(0,ω[-1])

axes[0].set_ylabel('|ŷ|')
plt.show()

#Truncating a discrete fourier transform to plot meaningful independent components (the one right above)
