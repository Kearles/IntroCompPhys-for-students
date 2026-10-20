#Lesson_16_practice
import matplotlib.pyplot as plt
import numpy as np


from scipy.constants import pi as π
from scipy.constants import g

"""# constants and intitial conditions
ℓ = 0.25 # m
Δt = 0.001 # s
T = 10 #total time s
n_steps = int(T / Δt)
#analytical solution: θ(t)= θ(o)cos(sqrt((g/ℓ)*t)))

θ = np.zeros(n_steps + 1)
ω = np.zeros(n_steps + 1)
t = np.arange(n_steps + 1) * Δt
#$\theta_0=\pi/12$ and $\dot{\theta}(0) =0$ for $\ell = 0.25$ m
θ[0] = π/12
ω[0] = 0
for n in range(n_steps):
    θ[n+1] = θ[n] + ω[n]*Δt
    ω[n+1] = ω[n] -(g/ℓ)*np.sin(θ[n])*Δt


fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(t, θ)
ax1.set_xlabel("Time [s]")
ax1.set_ylabel("Angle θ [rad]")

ax2.plot(θ, ω)
ax2.set_xlabel("Angle θ [rad]")
ax2.set_ylabel("Angular velocity ω [rad/s]")

plt.tight_layout()
plt.show()"""

#Euler Cromer method
# constants and intitial conditions
ℓ = 0.25 # m
Δt = 0.001 # s

t = np.arange(0.0,4.0,Δt)
θ,ω = np.zeros_like(t),np.zeros_like(t)
θ[0] = π/12.0 # rad

for n in range(t.size-1):
    pass

# the small angle solution
plt.plot(t, θ[0]*np.cos(np.sqrt(g/ℓ)*t), label='Small angle solution')

# the Euler-Cromer method
plt.plot(t,θ, label='Euler Cromer method')
plt.legend(loc='lower left',frameon=True)

plt.xlabel('Time [s]')
plt.ylabel('θ(t) [rad]')
plt.show()

#small angle solution.
def non_linear_θ(ℓ,θₒ,t):
    '''The solution for θ for the non-linear pendulum.'''
    # use special functions
    from scipy import special
    k = np.sin(θₒ/2.0)
    K = special.ellipk(k*k)
    (sn,cn,dn,ph) = special.ellipj(K-np.sqrt(g/l)*t,k*k)
    return 2.0*np.arcsin(k*sn)

#combining all solutions to one graph
# the small angle solution
plt.plot(t, θ[0]*np.cos(np.sqrt(g/ℓ)*t), label='Small angle solution')

# the Euler-Cromer method
plt.plot(t,θ,label='Euler Cromer method')

# the exact solution in terms of special functions
plt.plot(t,non_linear_θ(ℓ,θ[0],t), label='Exact', alpha=0.5)
plt.legend(loc='lower left',frameon=True)

plt.xlabel('Time [s]')
plt.ylabel('θ(t) [rad]')
plt.show()