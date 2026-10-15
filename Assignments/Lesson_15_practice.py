#Lesson_15_practice
import matplotlib.pyplot as plt
import numpy as np

from pathlib import Path



"""style_path = Path(__file__).resolve().parents[1] / 'include' / 'notebook.mplstyle'
plt.style.use(str(style_path))
#config InlineBackend.figure_format = 'svg'
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']"""

import scipy.constants as constants
def convert(value,unit1,unit2):
    '''Convert value in unit1 to unit2'''
    #converter
    conv = {'ft->m':constants.foot,'in->m':constants.inch,'mph->m/s':constants.mph}

    # make a copy and perform reverse conversions
    cpy_conv = dict(conv)
    
    for key, val in cpy_conv.items():
         
         units = key.split('->')
         conv[units[-1]+'->'+units[0]] = 1.0/val

        # perform the conversion
         key = '%s->%s'%(unit1,unit2)
         if key in conv:
            return value*conv[key]
         else:
             print('Unit conversion %s not possible.' %key)

def B2om(v): #defining the drag Coeff
    '''The drag Coefficient of a baseball.
       v in m/s
    '''
    vd = 35.0 # m/s
    Δ = 5.0 # m/s
    return 0.0039 + 0.0058/(1.0 + np.exp((v-vd)/Δ))

v = np.linspace(0,200,1000) #taking on values between 0 and 200. split into 1000 parts. so every 0.2.
"""plt.plot(v,B2om(convert(v,'mph','m/s'))*convert(1.0,'m','ft'))
plt.xlabel('Ball Speed [mph]')
plt.ylabel('Drag Coefficient [1/ft]')
plt.show()"""

from scipy.constants import g,pi
π = pi

# the time step
Δt = 0.001 # s

# the dimensionless angular drag factor
S0om = 4.1E-4

# the angular velocity
ω = 1900 * 2*π / 60 # rad/s

# initial conditions (convert everything to SI)
vx,vy,vz = convert(100,'mph','m/s'),0.0,0.0
r = [[0.0,convert(6.0+10.0/12.0,'ft','m'),0.0]]
print(r[-1][0])
while r[-1][0] <= convert(60.5,'ft','m'):
    v = np.sqrt(vx**2 + vy**2 + vz**2) #setting up V in each direction
    vx -= B2om(v)*v*vx*Δt
    vy -= g*Δt
    vz -= S0om*vx*ω*Δt
    r.append([r[-1][0]+vx*Δt,r[-1][1]+vy*Δt,r[-1][2]+vz*Δt])

# convert the result to feet
r = np.array(r)
r = convert(r,'m','ft') #conversions from converter set up before.

# Plot the resulting trajectory
fig, ax = plt.subplots(2, sharex=True)
fig.subplots_adjust(hspace=0.1)

# the x-y plane
ax[0].plot(r[:,0],r[:,1])
ax[0].set_ylabel('y [ft]')

# the y-z plane
ax[1].plot(r[:,0],r[:,2])
ax[1].set_ylabel('z [ft]')
ax[1].set_xlabel('x [ft]')
ax[1].set_xlim(0,60.5);

#modeling it in 3D using Matplotlib.
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(15,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(r[:,0], r[:,2], r[:,1], linewidth=3)
ax.dist = 12

ax.set_xlabel('x [ft]')
ax.set_ylabel('z [ft]')
ax.set_zlabel('y [ft]')
ax.set_zlim3d(0,7)
ax.set_xlim3d(0,60.5)

ax.xaxis.labelpad=30
ax.yaxis.labelpad=30
ax.zaxis.labelpad=15
#ax.view_init(0, -90) I think this is how to show the graph in a different view. It is.

plt.show()







#shoould graph movement of Knuckleball
def Fknuck(θ):
    '''The lateral acceleration on a knucleball in m/s^2'''
    from scipy.constants import g
    Fom = 0.5*g*(np.sin(4.0*θ) - 0.25*np.sin(8.0*θ) + \
                0.08*np.sin(12.0*θ) - 0.025*np.sin(16.0*θ))
    return Fom

θ = np.linspace(0,2*π,1000)
plt.plot(θ,Fknuck(θ))
plt.xlim(0,2*π);
plt.xlabel('θ [rad]')
plt.ylabel(r'$F/m\ [{\rm m/s^2}]$')

plt.show()