#Lesson_13_practice

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

style_path = Path(__file__).resolve().parents[2] / 'include' / 'notebook.mplstyle'
plt.style.use(str(style_path))
#config InlineBackend.figure_format = 'svg'
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

t = np.arange(0,10000,0.1)
plt.plot(t,np.sqrt(1+t))
plt.ylabel(r'$v(t)/v_0$')
plt.xlabel(r'$(2P/m v_0^2) t$')
plt.show()


Δt = 0.25 # s
m = 70 # kg
A = 0.33 # m^2
ρ = 1.2 # kg/m^3
P = 400 # W
vₒ = 4.0 # m/s

tmin,tmax,Δt = 0.0,100.0,0.5
from scipy.integrate import solve_ivp
t = np.arange(0,100,0.1)
for C in np.linspace(0,1,10):
    sol = solve_ivp(lambda t,v: P/(m*v) - (C*ρ*A/(2*m))*v**2, [np.min(t),np.max(t)],[4],t_eval=t)
    plt.plot(sol.t,sol.y[0,:],label=f'$C={C:.1f}$')

plt.legend(loc='upper left', ncol=2, fontsize=11)
plt.xlabel('Time [s]')
plt.ylabel('Speed [m/s]')
plt.show()

C = 0.5
sol = solve_ivp(lambda t,v: P/(m*v) - (C*ρ*A/(2*m))*v**2, [np.min(t),np.max(t)],[4],t_eval=t)
plt.plot(sol.t,sol.y[0,:],label=f'$C={C:.1f}$')

plt.legend(loc='upper left', ncol=2, fontsize=11)
plt.xlabel('Time [s]')
plt.ylabel('Speed [m/s]')
plt.show()