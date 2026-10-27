#Lesson_17_practice

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

def non_linear_θ(ℓ,θ0,t):
    '''The solution for θ for the non-linear pendulum.'''
    # use special functions
    from scipy import special
    k = np.sin(θ0/2.0)
    K = special.ellipk(k*k)
    (sn,cn,dn,ph) = special.ellipj(K-np.sqrt(g/l)*t,k*k) #these come from special?
    return 2.0*np.arcsin(k*sn)

from scipy.constants import pi as π
from scipy.constants import g

# constants and intitial conditions
ℓ = 0.25 # m
Δt = 0.001 # s

t = np.arange(0.0,4.0,Δt)
θ,ω = np.zeros_like(t),np.zeros_like(t)
θ[0] = π/4.0 # rad

for n in range(t.size-1):
    θ[n+1] = θ[n] + ω[n]*Δt
    ω[n+1] = ω[n] -(g/ℓ)*np.sin(θ[n+1])*Δt

# the exact solution
plt.plot(t,non_linear_θ(ℓ,θ[0],t), color=colors[0],label='Exact')

# the Euler-Cromer method
plt.plot(t[::20],θ[::20], 'o', mfc='None', markersize = 6, mec=colors[0],label='Euler Cromer method')
plt.legend(loc='lower left',frameon=True)

plt.xlabel('Time [s]')
plt.ylabel('θ(t) [rad]')
plt.show()

 
# For times <<1, we cann do discrete forward approximations to approximate continuous derivatives.
def euler(t,FD,ℓ,θ0,ω0,γ,ΩD): #defining the approx.
    ''' Semi-implicit Euler Method for the non-linear, dissipative, driven pendulum.'''
    
    Δt = t[1]-t[0]
    ω,θ = np.zeros_like(t),np.zeros_like(t)
    θ[0],ω[0] = θ0,ω0
    
    # perform the numerical integration
    for n in range(t.size-1):
        ω[n+1] = ω[n] + (-(g/ℓ)*np.sin(θ[n]) - γ*ω[n] + FD*np.sin(ΩD*t[n]))*Δt
        θ[n+1] = θ[n] + ω[n+1]*Δt
        
        # keep theta in [-pi,pi)
        if θ[n+1] < -π: θ[n+1] += 2.0*π
        if θ[n+1] >= π: θ[n+1] -= 2.0*π 

    return θ,ω

# This is for when there is a driving force affecting the time evolution
params = ℓ,θ0,ω0,γ,ΩD = g, 0.2, 0.0, 0.5, 2.0/3.0 #parameters definied for euler(ℓ,θ0,ω0,γ,ΩD) FD and t are below

FD = [0.0,0.5,0.75,1.0,1.25,1.5]

Δt = 0.04

t = np.arange(0.0,60,Δt)

#Graph setup for no driving force.
θ,ω = euler(t,0.0,*params)

plt.plot(t,θ)
plt.title(r'$F_\mathrm{D} = %3.1f\; \mathrm{s}^{-2}$' % 0.0)
plt.xlabel('Time [s]')
plt.ylabel('θ(t) [rad]')
plt.show()

#Setting up weak Driving Force
params = g, 0.2, 0.0, 0.5, 2.0/3.0
θ,ω = euler(t,0.2,*params) #note the change is 0 to 0.2

plt.plot(t,θ)
plt.title(r'$F_\mathrm{D} = %3.1f\; \mathrm{s}^{-2}$' % 0.2)
plt.xlabel('Time [s]')
plt.ylabel('θ(t) [rad]')
plt.show()

#Looking at how FD affects the time evolution.
""" 
F = [0.0,0.5,0.75,1.0,1.25,1.5]
# create a subplot array
fig, axes = plt.subplots(2,3, figsize=(12,10), sharex=True)

fig.subplots_adjust(wspace=0.3)

for i, ax in enumerate(axes.flat):

    θ,ω = euler(t,F[i],*params)

    ax.plot(t,θ, label=r'$F_\mathrm{D} = %3.1f\; \mathrm{s}^{-2}$' % F[i])

    ax.legend(frameon=True, loc='lower right')

# set axis labels
[ax.set_ylabel('θ(t) [rad]') for ax in axes[:,0]]
[ax.set_xlabel('Time [s]') for ax in axes[-1,:]]
plt.show()"""

"""#Testing different theta initial conditions
θ0 = [0.2,0.21,0.22] #  initial conditions
F = [0.5,1.2] # driving force (individually 0.5 and 1.2, No step between so only shows 2 graphs)

# compare the initial conditions
fig, axes = plt.subplots(2,1,sharex=True,sharey=False, figsize=(6,8))
for i, ax in enumerate(axes.flat):
    for j,cθ in enumerate(θ0):
        label = r'$\theta_0 = %4.2f\,\mathrm{rad}$' % cθ
        params = ℓ,cθ,ω0,γ,ΩD
        θ,ω = euler(t,F[i],*params)
        ax.plot(t,θ,label=label)
    ax.legend(frameon=True, loc='lower left')
    ax.text(70,0.0,r'$F_\mathrm{D} = %3.1f\; \mathrm{s}^{-2}$' % F[i],fontsize=30)
    
    # set axis labels
    ax.set_ylabel('θ(t) [rad]')

axes[-1].set_xlabel('Time [s]')
plt.show()"""

#Looking at Δθ
F = [0.5,1.2] # driving force [1/s^2]
θ0 = 0.2 # initial angle [rad]
params = [(ℓ,θ0,ω0,γ,ΩD),(ℓ,θ0+1.0E-4,ω0,γ,ΩD)]

Δθ = []
fig, axes = plt.subplots(2,1,sharex=True, sharey=False, squeeze=False, figsize=(6,8))
for i, ax in enumerate(axes.flat):
    label = r'$F_\mathrm{D} = %3.1f\; \mathrm{s}^{-2}$' % F[i]
    
    θ1,ω = euler(t,F[i],*params[0])
    θ2,ω = euler(t,F[i],*params[1])
    Δθ.append(np.abs(θ1-θ2))
    
    ax.semilogy(t, Δθ[i], label=label)
    ax.legend(loc='best', frameon=False)
    
    # set axis labels
    ax.set_ylabel('|Δθ(t)| [rad]')

axes[1,0].set_xlabel('Time [s]')
plt.show()

#scipy.signal.argrelextrema = finds local minima and maxima
#scipy.optimize.curve_fit = general curve fitting

from scipy.signal import argrelextrema
from scipy.optimize import curve_fit

F = [0.5,1.2]

#defininf the linear fitting funciton
def linear(x,a0,a1): 
    return a0 + a1*x

# find the local maxima and perform the fit
popt = [0,0]
for i,cF in enumerate(F):
    ind = argrelextrema(np.log(Δθ[i]),np.greater)[0]
    popt[i], pcov = curve_fit(linear,t[ind],np.log(Δθ[i][ind]))

fig, axes = plt.subplots(2,1,sharex=True, sharey=False, squeeze=False, figsize=(6,8))
for i, ax in enumerate(axes.flat):
    labellam = r'$\lambda = %4.2f\; \mathrm{s}^{-1}$' % popt[i][1]
    
    ax.semilogy(t, Δθ[i], ',', markeredgewidth=0.0)
    ax.semilogy(t, np.exp(linear(t,*popt[i])), linewidth=3.0, label=labellam, color=colors[0])
      
    # set labels and legend
    ax.set_ylabel('|Δθ(t)| [rad]')
    ax.text(70,1.0E-6,r'$F_\mathrm{D} = %3.1f\; \mathrm{s}^{-2}$' % F[i],fontsize=30)
    ax.legend()
axes[1,0].set_xlabel('Time [s]')
plt.show()

#We need to generate a label for the driving force.
def FD_label(Fd):
    '''Create a label based on the value of FD'''
    return f'$F_\mathrm{{D}} = {F[i]:G}\; \mathrm{{s}}^{{-2}}$'

#Use ax.text and transforms=ax.transAxes to label plots.

params = ℓ,θ0,ω0,γ,ΩD
F = [0.5,1.2]

fig, axes = plt.subplots(2,1,sharex=True, sharey=False, squeeze=False, figsize=(6,8))
for i, ax in enumerate(axes.flat):
    θ,ω = euler(t,F[i],*params)
    
    ax.plot(θ,ω,marker='o', linestyle='None', ms=1)
    
    # set axis labels and legends
    ax.set_ylabel('ω [rad/s]')
    ax.set_xlim(-π,π)
    ax.text(1.05,0.5,FD_label(F[i]),fontsize=30,transform=ax.transAxes)

axes[1,0].set_xlabel('θ(t) [rad]')
plt.show()

#notice how for small diriving forces, we observe the bottom graph, and for large driving forces, its nearly closed like the top graph.

Δt = 2.0*π/(ΩD*100)
longt = np.arange(0,10000,Δt)

F = [0.5,1.2]
θ,ω = [],[]
for cF in F:
    th,w = euler(longt,cF,*params)
    θ.append(th)
    ω.append(w)

#determine the pstep corrresponding to the in phase times

T = 2*π/ΩD
pstep = int(T/Δt + 0.5)
inPhaset = longt[::pstep]
print(inPhaset)
print(pstep) # =100

#Now we plot the actual solution

pcol = colors[1],colors[-2]
plt.figure(figsize=(8,8))
for i in range(2):
    plt.plot(θ[i][::pstep], ω[i][::pstep], marker='o', color=pcol[i], ms=3, linestyle='None', label=FD_label(F[i]), alpha=0.5)
    
plt.title('Strange Attractors')
plt.legend(fontsize=16, handletextpad=0.2, markerscale=2)
plt.xlabel('θ [rad]')
plt.ylabel('ω [rad/s]')
plt.xlim(-π,π);
plt.show()

#We get two points in non-chaotic regime. We have a fuzzy surface in the chaotic regime.


#Bifurcation Diragram
#looking at long term behavior of system after transients died out as a function of F_D

run = False
F = np.arange(0,1.5,0.0025)
theta_data = Path(__file__).resolve().parents[2] / 'data' / 'theta.dat'
if run:
    θ = np.zeros([len(longt[10*pstep::pstep]),len(F)])
    for i,cF in enumerate(F):
        th,ω = euler(longt,cF,*params)
        θ[:,i] = th[10*pstep::pstep]
    np.savetxt(theta_data,θ)
else:
    θ = np.loadtxt(theta_data)

plt.figure(figsize=(7,7))
pF = np.ones_like(θ[:,0])
for i,cF in enumerate(F):
    u = np.unique(θ[:,i])
    pF = cF*np.ones_like(u)
    plt.plot(pF, u, marker='o', ms=3, linestyle='None', mfc=colors[1], mew=0, mec='None', alpha=1,rasterized=True) 

plt.ylabel('θ [rad]')
plt.xlabel(r'$F_\mathrm{D}\; [\mathrm{s}^{-2}]$')
plt.xlim(1.34,1.5);
plt.ylim(0,π);
plt.show()
