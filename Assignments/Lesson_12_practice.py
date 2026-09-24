# lesson_12_practice
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

#matplotlib inline
style_path = Path(__file__).resolve().parent.parent / 'include' / 'notebook.mplstyle'
plt.style.use(str(style_path))
#config InlineBackend.figure_format = 'svg'
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

#graph setup
t = np.arange(0,5,0.1) 
plt.plot(t,np.exp(-t), label='Exact Solution')
plt.ylabel(r'$N(t)/N_0$')
plt.xlabel(r'$t/\tau$')
plt.show() 

#Write a program that employs the Euler Method to solve the radioactive decay problem and compare with the exact solution.

#dN(t)/dt = -N/tau  

# lines 7-16 graph exact solutiton
#Euler approximation is N*(t+ Delta t) approx equal to (1 - (Delta t)/t) * N(t))

# define array t/tau = n * Delta t where n \in \mathbb{Z} is an integer
#accuracy should depend on Delta t

# Euler approximation for radioactive decay
# dN/dt = -N / tau, with N(0) = N0
# Euler update: N_{n+1} = N_n - dt * N_n / tau

tau = 1.0
N0 = 1.0

dt = 0.5
n_steps = 10

t = np.arange(0, n_steps * dt + dt, dt)
N = np.zeros_like(t)
N[0] = N0

for n in range(1, len(t)):
    N[n] = N[n - 1] - dt * N[n - 1] / tau

plt.figure()
plt.plot(t, N, 'o-', label='Euler approximation', linewidth=2)
plt.ylabel(r'$N(t)/N_0$')
plt.xlabel(r'$t/\tau$')
plt.title('Euler Approximation to Radioactive Decay')
plt.legend()
plt.show()

# exact solution for comparison
t_exact = np.linspace(0, 5, 500)
N_exact = np.exp(-t_exact)

# plot both on the same graph
plt.figure()
plt.plot(t_exact, N_exact, label='Exact solution', linewidth=2)
plt.plot(t, N, 'o--', label=f'Euler approximation (dt = {dt})', linewidth=2)

plt.ylabel(r'$N(t)/N_0$')
plt.xlabel(r'$t/\tau$')
plt.title('Radioactive decay: exact vs Euler approximation')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

