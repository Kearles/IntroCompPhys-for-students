#Lesson_18_practice
import matplotlib.pyplot as plt
import numpy as np

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

#Completing the function to return the full solution of the Logistic Map
def logistic_map(x,μ):
    '''Return the iterative logistic map.'''

    # INSERT CODE HERE
                        #x_{n+1} =  μ*x_n (1 - x_n) logistic map equation
    for n in range(x.size-1):
        x[n+1] = μ*x[n]*(1-x[n])
    pass

    return x

def μ_lab(μ):
    return f'$\mu =  {μ:G}$'

N = 100
μ = [1.5,3.3,3.8]
x = np.random.random(N)

fig, axes = plt.subplots(3,1,sharex=True, sharey=True, squeeze=False, figsize=(7,8))
for i, ax in enumerate(axes.flat):
    
    # iterate the map
    x = logistic_map(x,μ[i])
    
    # plot the numerical results
    ax.plot(x,linestyle='-',marker='o',linewidth=1.0,markerfacecolor='None', 
            color=colors[i], markeredgecolor=colors[i], markersize=3, 
            label=μ_lab(μ[i]))
    ax.legend(loc='lower right', frameon=True)
    ax.set_ylabel('x')
    ax.set_ylim(0,1)

axes[-1,0].set_xlabel('n')
plt.show()




#identifying the fixed point via brute force integration
x = [np.random.random()]
cμ = 3

# the first iteration
x.append(cμ*x[0]*(1-x[0]))

# continue until we find a fixed point
n = 0
while np.abs(x[-1]-x[-2]) > 1.0E-6 and n < 200:
    x.append(cμ*x[-1]*(1-x[-1]))
    n += 1             #checking next value adding +1 to n until 200
pass

plt.plot(x, color=colors[0],label=f'x* = {x[-1]:G}', linewidth=1, alpha=0.5)
plt.axhline(y=(1.0-1.0/cμ), color=colors[1], linestyle='--', label=f'1-1/μ = {1-1/cμ:G}')
plt.ylim(0,1)
plt.xlabel('n')
plt.ylabel('x')
plt.legend(frameon=True)
plt.show()


#plotting x_n vs x_n+1
μ = [1.5,3.3]
x = np.arange(0,1.01,0.01)
fig, axes = plt.subplots(1,2,sharex=True, sharey=True, squeeze=False, figsize=(10,5))
fig.subplots_adjust(wspace=0.3)
for i, ax in enumerate(axes.flat):
    
    # plot x
    ax.plot(x,x,color='k')
    
    # plot f(x,μ)
    ax.plot(x,μ[i]*x*(1-x),color=colors[i], label=μ_lab(μ[i]))
    
    # plot the fixed point solutions
    ax.plot(0,0,'o',markersize=15, markerfacecolor=colors[-3], markeredgecolor='w')
    ax.plot(1-1/μ[i],1-1/μ[i],'o',markersize=10, markerfacecolor=colors[-3], markeredgecolor='w')
            
    ax.legend(loc='upper left', frameon=True)
    ax.set_xlabel(r'$x_n$')
    
    ax.set_ylim(0,1)
    ax.set_xlim(0,1)
axes[0,0].set_ylabel(r'$x_{n+1}$')
plt.show()


#Mapping the equivalent of a Phase space
def logistic(mu,x):
    '''Return the logistic functon'''
    return mu*x*(1.0-x)

μ = [1.5,3.3]
x = np.arange(0,1,0.01)
xp = np.zeros([N,2])
xp[0,0] = np.random.random()
xp[0,1] = 0.0

fig, axes = plt.subplots(1,2,sharex=True, sharey=True, squeeze=False, figsize=(10,5))
fig.subplots_adjust(wspace=0.3)
for i, ax in enumerate(axes.flat):
    # plot x
    ax.plot(x,x,color='k')

    # plot f(x,μ)
    ax.plot(x,μ[i]*x*(1-x),color=colors[i], label=μ_lab(μ[i]))

    # compute the trajectories
    for n in range(1,N-1,2):
        xp[n,0] = xp[n-1,0]
        xp[n,1] = logistic(μ[i],xp[n-1,0])
        xp[n+1,0] = xp[n,1]
        xp[n+1,1] = xp[n,1]

    ax.plot(xp[:,0],xp[:,1],'--',color=colors[-3],linewidth=1)

    # legend and labels
    ax.legend(loc='upper right', frameon=True)
    ax.set_xlabel(r'$x_n$')
    
    ax.set_ylim(0,1)
    ax.set_xlim(0,1)
    
axes[0,0].set_ylabel(r'$x_{n+1}$')
plt.show()


#Find a graphical solution to the second iterate of the Logistic map and plot for μ =1.5,3.3
μ = [1.5,3.3]
x = np.arange(0,1.01,0.01)
fig, axes = plt.subplots(1,2,sharex=True, sharey=True, squeeze=False, figsize=(10,5))
fig.subplots_adjust(wspace=0.3)
xp = np.zeros([N,2])
xp[0,0] = np.random.random()
xp[0,1] = 0.0
for i, ax in enumerate(axes.flat):
    
    # plot x
    ax.plot(x,x,color='k')

    fx = μ[i]*x*(1-x)
    #need to plot f(f(x,μ),u))
    ax.plot(x,μ[i]*fx*(1-fx),color=colors[i], label=μ_lab(μ[i]))
    pass

    # compute the trajectories
    for n in range(1,N-1,2):
        xp[n,0] = xp[n-1,0]
        xp[n,1] = logistic(μ[i],xp[n-1,0])
        xp[n+1,0] = xp[n,1]
        xp[n+1,1] = xp[n,1]

    ax.plot(xp[:,0],xp[:,1],'--',color=colors[-3],linewidth=1)            
    ax.legend(loc='upper left', frameon=True)
    
axes[0,0].set_ylabel(r'$x_{n+2}$')
[axes[0,i].set_xlabel(r'$x_n$') for i in range(2)]
axes[0,0].set_ylim(0,1)
axes[0,0].set_xlim(0,1)
plt.show()